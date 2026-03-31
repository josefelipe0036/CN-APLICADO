# Simulação Numérica de Sedimentação de Esferas (RK4)

 Este projeto implementa um solver numérico em Python para descrever a dinâmica de uma esfera sólida sedimentando em um fluido viscoso.  O objetivo é analisar o comportamento da velocidade da partícula em diferentes regimes de escoamento, do limite de Stokes ($Re \to 0$) até efeitos inerciais moderados ($Re \sim 1$).

## 1\. Fundamentação Teórica

 A simulação baseia-se na **equação diferencial adimensional** derivada na Atividade para Casa (APC), que descreve a aceleração da esfera sob a influência da gravidade, empuxo e forças de arrasto (Stokes e Oseen):



$$
St \frac{dv_z^*}{dt^*} = 1 - v_z^* - \frac{3}{8} Re_s (v_z^*)^2
$$

### Parâmetros Físicos:

  *  **Número de Stokes ($St$):** Razão entre a escala de tempo de relaxação da partícula e o tempo convectivo do fluido.
  *  **Número de Reynolds de partícula ($Re_s$):** Parâmetro que mede a importância relativa das forças inerciais frente às viscosas.
  *  **Variáveis Adimensionais ($v_z^*$ e $t^*$):** Velocidade e tempo normalizados para garantir a universalidade do modelo.

## 2\. Método Numérico: Runge-Kutta de 4ª Ordem (RK4)

 Para a integração temporal da EDO, utiliza-se o método de **Runge-Kutta de quarta ordem clássico**.Este método oferece um erro de truncamento global de $O(h^4)$, sendo superior ao método de Euler simples.

 O algoritmo calcula quatro inclinações intermediárias ($k_1, k_2, k_3, k_4$) em cada passo de tempo para determinar o próximo valor da velocidade.

## 3\. Descrição do Programa

### Entradas (Inputs)

 O simulador requer os seguintes parâmetros definidos no início da execução:

  * `St`: O número de Stokes (ex: 0.1, 0.5, 2.0).
  * `Res`: O número de Reynolds da partícula (0 para regime de Stokes, $>0$ para inercial).
  *  `h`: O passo de tempo para o refinamento da malha temporal.
  * `t_final`: O tempo total da simulação.

### Processamento

1.   **Inicialização:** Define a velocidade inicial $v_z^*(0) = 0$ (partícula partindo do repouso).
2.   **Iteração RK4:** Avança no tempo calculando os coeficientes $k_i$ e atualizando a velocidade em cada passo $h$.
3.   **Validação:** Compara os resultados numéricos com as soluções analíticas disponíveis no material (Solução de Ricatti e Exponencial).

### Saídas (Outputs)

  *  **Vetores de Dados:** Conjunto de dados contendo o histórico de tempo e velocidade.
  *  **Gráficos:** Curvas de sedimentação comparando o comportamento numérico com o padrão ouro (analítico).

## 4\. Requisitos de Execução

  *  O código foi desenvolvido de forma nativa, utilizando apenas estruturas básicas da linguagem (vetores, funções e laços), conforme as restrições da atividade.
  * Requer **Python 3.x** e as bibliotecas `numpy` e `matplotlib` para visualização dos dados.


**Autor:** José Felipe (Estatística - UnB)
**Data:** Março de 2026
**Repositório:** [josefelipe0036/CN-APLICADO](https://www.google.com/search?q=https://github.com/josefelipe0036/CN-APLICADO)
