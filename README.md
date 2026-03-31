# 🧪 Simulação Numérica de Sedimentação de Esferas (RK4)

Este projeto implementa um solver numérico em Python para descrever a dinâmica de uma esfera sólida sedimentando em um fluido viscoso. O objetivo é analisar o comportamento da velocidade da partícula em diferentes regimes de escoamento, do limite de Stokes ($Re \to 0$) até efeitos inerciais moderados ($Re \sim 1$).

---

## 📚 1. Fundamentação Teórica

A simulação baseia-se na **equação diferencial adimensional**:

$$
St \cdot \frac{d v_z^*}{dt^*} = 1 - v_z^* - \frac{3}{8} Re_s (v_z^*)^2
$$

### 🔎 Parâmetros Físicos

- **Número de Stokes ($St$):** razão entre o tempo de relaxação da partícula e o tempo convectivo do fluido.
- **Número de Reynolds da partícula ($Re_s$):** mede a importância relativa entre forças inerciais e viscosas.
- **Variáveis adimensionais ($v_z^*$, $t^*$):** tornam o modelo independente de escala física.

---

## ⚙️ 2. Método Numérico: Runge-Kutta de 4ª Ordem (RK4)

A EDO é resolvida utilizando o método clássico de Runge-Kutta de quarta ordem.

Dado:

$$
\frac{dv}{dt} = f(t, v)
$$

O esquema RK4 é:

$$
\begin{aligned}
k_1 &= f(t_n, v_n) \\
k_2 &= f\left(t_n + \frac{h}{2}, v_n + \frac{h}{2}k_1\right) \\
k_3 &= f\left(t_n + \frac{h}{2}, v_n + \frac{h}{2}k_2\right) \\
k_4 &= f(t_n + h, v_n + hk_3) \\
\\
v_{n+1} &= v_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)
\end{aligned}
$$

✔️ Erro global: $O(h^4)$  
✔️ Alta estabilidade para EDOs não lineares

---

## 💻 3. Descrição do Programa

### 📥 Entradas

- `St`: número de Stokes (ex: 0.1, 0.5, 2.0)
- `Res`: número de Reynolds da partícula
- `h`: passo de tempo
- `t_final`: tempo final da simulação

---

### 🔄 Processamento

1. Inicialização:
   $$
   v_z^*(0) = 0
   $$

2. Iteração RK4:
   - cálculo de $k_1, k_2, k_3, k_4$
   - atualização da velocidade

3. Validação:
   - comparação com soluções analíticas:
     - regime de Stokes → solução exponencial
     - regime com inércia → equação de Riccati

---

### 📤 Saídas

- Vetores:
  - tempo $t$
  - velocidade $v_z^*(t)$
- Gráficos:
  - curva numérica vs solução analítica

---

## ▶️ 4. Requisitos

- Python 3.x
- Bibliotecas:
  ```bash
  pip install numpy matplotlib
