import numpy as np
import matplotlib.pyplot as plt

class RungeKuttaExplicito:
    def __init__(self, ordem):
        """
        Inicializa o solver com o Tableau de Butcher correspondente à ordem desejada.
        """
        self.ordem = ordem
        self.A, self.b, self.c = self._get_butcher_tableau(ordem)
        self.estagios = len(self.b)
        
    def _get_butcher_tableau(self, ordem):
        """
        Retorna os coeficientes A (matriz), b (pesos) e c (nós de tempo).
        """
        if ordem == 1:
            # RK1 (Método de Euler)
            A = np.array([[0]])
            b = np.array([1])
            c = np.array([0])
            
        elif ordem == 2:
            # RK2 (Método de Heun / Ponto Médio)
            A = np.array([[0,   0],
                          [0.5, 0]])
            b = np.array([0, 1])
            c = np.array([0, 0.5])
            
        elif ordem == 3:
            # RK3 Clássico
            A = np.array([[0,   0,   0],
                          [0.5, 0,   0],
                          [-1,  2,   0]])
            b = np.array([1/6, 2/3, 1/6])
            c = np.array([0, 0.5, 1])
            
        elif ordem == 4:
            # RK4 Clássico
            A = np.array([[0,   0,   0,   0],
                          [0.5, 0,   0,   0],
                          [0,   0.5, 0,   0],
                          [0,   0,   1,   0]])
            b = np.array([1/6, 1/3, 1/3, 1/6])
            c = np.array([0, 0.5, 0.5, 1])
            
        elif ordem == 5:
            # RK5 (Método de Butcher de 5ª ordem, exige 6 estágios)
            A = np.array([
                [0,           0,           0,          0,         0,    0],
                [1/4,         0,           0,          0,         0,    0],
                [1/8,         1/8,         0,          0,         0,    0],
                [0,           0,           1/2,        0,         0,    0],
                [3/16,       -3/8,         3/8,        9/16,      0,    0],
                [-3/7,        8/7,         6/7,       -12/7,      8/7,  0]
            ])
            b = np.array([7/90, 0, 32/90, 12/90, 32/90, 7/90])
            c = np.array([0, 1/4, 1/4, 1/2, 3/4, 1])
            
        else:
            raise NotImplementedError(
                f"Ordem {ordem} não está pre-configurada. "
                "Para ordens >= 6, as matrizes de Butcher são muito densas (ex: RK10 tem 17 estágios). "
                "Insira manualmente os coeficientes na função _get_butcher_tableau ou use scipy.integrate."
            )
            
        return A, b, c

    def resolver(self, f, t_span, y0, h):
        """
        Resolve o Problema de Valor Inicial (PVI).
        """
        t0, tf = t_span
        t = np.arange(t0, tf + h, h)
        
        # Identifica se é uma única equação (escalar) ou sistema (vetor)
        is_scalar = isinstance(y0, (int, float))
        
        if is_scalar:
            y = np.zeros(len(t))
            y[0] = y0
            # Aloca K como um vetor 1D simples
            K = np.zeros(self.estagios)
        else:
            y = np.zeros((len(t), len(y0)))
            y[0] = np.array(y0)
            # Aloca K como matriz 2D para sistemas
            K = np.zeros((self.estagios, len(y0)))
            
        for n in range(len(t) - 1):
            y_atual = y[n]
            t_atual = t[n]
            
            for i in range(self.estagios):
                soma_k = np.zeros_like(y_atual, dtype=float)
                for j in range(i):
                    soma_k += self.A[i, j] * K[j]
                
                t_estimado = t_atual + self.c[i] * h
                y_estimado = y_atual + h * soma_k
                
                # Atribuição direta e limpa para K[i]
                valor_f = f(t_estimado, y_estimado)
                if is_scalar:
                    K[i] = valor_f
                else:
                    K[i] = np.array(valor_f).flatten()
            
            y[n+1] = y_atual + h * np.dot(self.b, K)
            
        return t, y

# =====================================================================
# Exemplo de uso
# =====================================================================
if __name__ == "__main__":
    # Definimos uma EDO teste: dy/dt = -2y + t^2
    def edo_teste(t, y):
        return -2 * y + t**2

    t_inicial = 0
    t_final = 2
    y_inicial = 1
    passo = 0.2

    # Loop para demonstrar as ordens de 1 até 5
    for p in range(1, 6):
        rk = RungeKuttaExplicito(ordem=p)
        tempo, solucao = rk.resolver(edo_teste, (t_inicial, t_final), y_inicial, passo)
        plt.plot(tempo, solucao, marker='o', label=f'RK Ordem {p}')

    plt.title('Comparação EDO: $dy/dt = -2y + t^2$')
    plt.xlabel('Tempo (t)')
    plt.ylabel('Solução (y)')
    plt.legend()
    plt.grid()
    plt.show()