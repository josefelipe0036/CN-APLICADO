# Simulação Numérica de Sedimentação de Esferas (RK4)

[cite_start]Este projeto implementa um solver numérico em Python para descrever a dinâmica de uma esfera sólida sedimentando em um fluido viscoso[cite: 152]. [cite_start]O objetivo é analisar o comportamento da velocidade da partícula em diferentes regimes de escoamento, do limite de Stokes ($Re \to 0$) até efeitos inerciais moderados ($Re \sim 1$)[cite: 56, 116].

## 1\. Fundamentação Teórica

[cite_start]A simulação baseia-se na **equação diferencial adimensional** derivada na Atividade para Casa (APC), que descreve a aceleração da esfera sob a influência da gravidade, empuxo e forças de arrasto (Stokes e Oseen)[cite: 62, 67, 137]:

$$St \frac{dv_z^*}{dt^*} = 1 - v_z^* - \frac{3}{8} Re_s (v_z^*)^2$$

### Parâmetros Físicos:

  * [cite_start]**Número de Stokes ($St$):** Razão entre a escala de tempo de relaxação da partícula e o tempo convectivo do fluido[cite: 47].
  * [cite_start]**Número de Reynolds de partícula ($Re_s$):** Parâmetro que mede a importância relativa das forças inerciais frente às viscosas[cite: 74, 138].
  * [cite_start]**Variáveis Adimensionais ($v_z^*$ e $t^*$):** Velocidade e tempo normalizados para garantir a universalidade do modelo[cite: 42, 70].

## 2\. Método Numérico: Runge-Kutta de 4ª Ordem (RK4)

[cite_start]Para a integração temporal da EDO, utiliza-se o método de **Runge-Kutta de quarta ordem clássico**[cite: 128]. [cite_start]Este método oferece um erro de truncamento global de $O(h^4)$, sendo superior ao método de Euler simples[cite: 130, 131].

[cite_start]O algoritmo calcula quatro inclinações intermediárias ($k_1, k_2, k_3, k_4$) em cada passo de tempo para determinar o próximo valor da velocidade[cite: 131, 143].

## 3\. Descrição do Programa

### Entradas (Inputs)

[cite_start]O simulador requer os seguintes parâmetros definidos no início da execução[cite: 146]:

  * `St`: O número de Stokes (ex: 0.1, 0.5, 2.0).
  * `Res`: O número de Reynolds da partícula (0 para regime de Stokes, $>0$ para inercial).
  * [cite_start]`h`: O passo de tempo para o refinamento da malha temporal[cite: 155].
  * `t_final`: O tempo total da simulação.

### Processamento

1.  [cite_start]**Inicialização:** Define a velocidade inicial $v_z^*(0) = 0$ (partícula partindo do repouso)[cite: 48].
2.  [cite_start]**Iteração RK4:** Avança no tempo calculando os coeficientes $k_i$ e atualizando a velocidade em cada passo $h$[cite: 144].
3.  [cite_start]**Validação:** Compara os resultados numéricos com as soluções analíticas disponíveis no material (Solução de Ricatti e Exponencial)[cite: 49, 79, 157].

### Saídas (Outputs)

  * [cite_start]**Vetores de Dados:** Conjunto de dados contendo o histórico de tempo e velocidade[cite: 147].
  * [cite_start]**Gráficos:** Curvas de sedimentação comparando o comportamento numérico com o padrão ouro (analítico)[cite: 158, 163].

## 4\. Requisitos de Execução

  * [cite_start]O código foi desenvolvido de forma nativa, utilizando apenas estruturas básicas da linguagem (vetores, funções e laços), conforme as restrições da atividade[cite: 160, 161].
  * Requer **Python 3.x** e as bibliotecas `numpy` e `matplotlib` para visualização dos dados.


**Autor:** José Felipe (Estatística - UnB)
**Data:** Março de 2026
**Repositório:** [josefelipe0036/CN-APLICADO](https://www.google.com/search?q=https://github.com/josefelipe0036/CN-APLICADO)
