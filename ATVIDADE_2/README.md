
# APC2: Localização de Raízes de Polinômios - Método de Bairstow

Este repositório contém a implementação da **Atividade e Programa para Casa #2** da disciplina de **Cálculo Numérico Aplicado**, ministrada pelo Prof. Dr. Rafael Gabler Gontijo. O objetivo é utilizar o método de Bairstow para encontrar raízes reais e complexas de polinômios e visualizar o comportamento de convergência através de fractais.

## 1. Fundamentação Teórica
O Método de Bairstow é uma técnica iterativa que extrai pares de raízes (reais ou complexas) de um polinômio $P_n(x)$ dividindo-o sucessivamente por um fator quadrático $x^2 - rx - s$. 

Diferente do método de Newton-Raphson tradicional, Bairstow opera exclusivamente com aritmética real para encontrar raízes complexas conjugadas, o que o torna eficiente para sistemas dinâmicos regidos por EDOs de 2ª ordem, como:
$$a_2 \frac{d^2y}{dt^2} + a_1 \frac{dy}{dt} + a_0 y = F(t)$$

## 2. Entradas e Saídas do Programa

O script foi desenvolvido em **Python** (ou R), utilizando apenas operações matriciais básicas e laços de repetição, conforme os requisitos da atividade.

### **Entradas (Inputs)**
* **Coeficientes do Polinômio ($a_n, \dots, a_0$):** Lista de valores numéricos que representam o sistema físico.
* **Valores Iniciais ($r_0, s_0$):** Chutes iniciais para o fator quadrático. No caso da geração do fractal, estas entradas são substituídas por um *grid* de valores no plano bidimensional.
* **Tolerância ($\epsilon$):** Erro máximo permitido para a convergência (ex: $10^{-5}$).
* **Máximo de Iterações:** Critério de parada para evitar loops infinitos em regiões de divergência.

### **Saídas (Outputs)**
* **Raízes Calculadas:** Lista das $n$ raízes do polinômio (formatadas como números complexos).
* **Análise de Estabilidade:** Diagnóstico do sistema baseado na parte real das raízes:
    * $\text{Re}(x) < 0$: Sistema **Estável**.
    * $\text{Re}(x) > 0$: Sistema **Instável**.
* **Fractal de Bairstow:** Imagem (mapa de calor) que representa a bacia de atração. Cada cor indica o número de iterações necessárias para convergir a partir de um par $(r_0, s_0)$ específico.

## 3. Estrutura do Código
1.  **Divisão Sintética:** Função que calcula os coeficientes $b$ (resto) e $c$ (derivadas parciais).
2.  **Iteração de Bairstow:** Resolução do sistema jacobiano $2 \times 2$ para atualização de $r$ e $s$.
3.  **Deflação:** Redução do grau do polinômio após a convergência de cada par de raízes.
4.  **Mapeamento de Fractal:** Loop que varre o plano $(r, s)$ e gera a visualização via `matplotlib`.


## 4. Referências
* **Chapra, S. C.; Canale, R. P.** *Métodos Numéricos para Engenharia*. McGraw Hill, 5ª edição, 2008.
* **Gontijo, R. G.** *Notas de aula do curso de Cálculo Numérico Aplicado*, 2026.

