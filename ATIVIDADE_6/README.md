# Solução Numérica para Condução de Calor em Aleta 2D (PPC6)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Este repositório contém a implementação numérica computacional da Atividade e Programa para Casa #6 (PPC6) da disciplina de Cálculo Numérico Aplicado (Universidade de Brasília - UnB). 

O projeto resolve o problema bidimensional de condução de calor em regime permanente para uma aleta retangular de seção transversal constante, utilizando o **Método das Diferenças Finitas (MDF)** aplicado à Equação de Laplace.

$$ \frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} = 0 $$

---

##  Metodologia Implementada

O domínio espacial da aleta foi discretizado em uma malha estruturada, e as derivadas parciais foram aproximadas por diferenças finitas centradas de ordem $\mathcal{O}(\Delta x^2)$. O código resolve o sistema linear esparso gerado através de três abordagens distintas para fins de comparação de desempenho numérico:

1. **Eliminação de Gauss** (Método Direto)
2. **Método de Liebmann (Gauss-Seidel)** (Método Iterativo sem relaxação)
3. **Método de Liebmann com Sobre-relaxação (SOR)** (Método Iterativo acelerado)

---

##  Entradas (Inputs)

O programa interage com o usuário via terminal (ou pode ser configurado diretamente no script) para receber os parâmetros físicos e computacionais necessários para a simulação. 

| Categoria | Parâmetro | Símbolo | Unidade | Descrição |
| :--- | :--- | :---: | :---: | :--- |
| **Geometria** | Comprimento da aleta | $L$ | $m$ | Dimensão total da aleta na direção $x$. |
| | Espessura da aleta | $H$ | $m$ | Dimensão total da aleta na direção $y$. |
| **Propriedades** | Condutividade térmica | $k$ | $W/m\cdot K$ | Propriedade de transporte de calor do material. |
| | Coeficiente convectivo | $h$ | $W/m^2\cdot K$ | Coeficiente de troca de calor com o fluido externo. |
| **Contornos**| Temperatura da base | $T_b$ | $^\circ C$ | Condição de Dirichlet na face esquerda ($x = 0$). |
| | Temperatura ambiente | $T_\infty$ | $^\circ C$ | Condição de Robin (convecção) nas demais faces. |
| **Numéricos** | Número de nós em $x$ e $y$ | $N_x, N_y$ | - | Define o refinamento da malha de diferenças finitas. |
| | Tolerância de convergência | $tol$ | $\%$ | Erro relativo máximo aceitável para interrupção iterativa. |
| | Fator de relaxação | $\omega$ | - | Parâmetro de aceleração do SOR ($1 < \omega < 2$). |

---

## Saídas (Outputs)

Após o processamento, o código entrega os resultados em três formatos distintos para facilitar a análise dos dados espaciais e do custo computacional.

### 1. Métricas no Console
* **Tempo Computacional:** Tempo total de execução (em segundos) para cada um dos três métodos avaliados (Gauss, Liebmann, SOR).
* **Convergência:** Número exato de iterações requeridas pelos métodos iterativos e o erro final atingido.
* **Validação Analítica:** O erro percentual médio obtido pela comparação entre a temperatura na linha central da aleta ($2D$) e a solução analítica clássica hiperbólica para uma aleta $1D$.

### 2. Exportação de Dados
* Arquivos tabulares (`.csv` ou `.txt`) contendo as matrizes exportadas do domínio espacial.
* Colunas principais exportadas: `Coordenada X`, `Coordenada Y` e `Temperatura (T)` para todos os nós processados na malha.

### 3. Visualização Gráfica
O código utiliza o `matplotlib` para renderizar automaticamente três representações visuais:
* **Mapa de Calor 2D (Colormap):** Uma visualização em cores representando o campo contínuo de temperaturas distribuído ao longo de toda a seção transversal da aleta.
* **Curvas de Nível (Isotermas):** Contornos delimitando as zonas de mesma temperatura no domínio.
* **Gráfico de Linha Central (1D vs 2D):** Gráfico de linha comparando ponto a ponto a distribuição de temperatura ao longo do eixo central ($y = H/2$) extraída do modelo numérico $2D$ contra a curva da solução analítica $1D$.

---
