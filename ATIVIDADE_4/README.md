# PPC4: Otimização Multidimensional Sem Restrições

Este repositório contém a implementação da **Atividade e Programa para Casa #4** da disciplina de **Cálculo Numérico Aplicado**, ministrada pelo Prof. Dr. Rafael Gabler Gontijo. O objetivo é implementar métodos clássicos de otimização multidimensional sem restrições baseados no cálculo de gradientes e visualizar o comportamento de convergência de cada estratégia.

## 1. Fundamentação Teórica

O problema proposto consiste na maximização da seguinte função objetivo quadrática:


$$f(x,y) = 2xy + 2x - x^2 - 2y^2$$

Cujo ponto ótimo analítico localiza-se em $(x^*, y^*) = (2, 1)$, em que $f^* = 2$. Para alcançar este ponto a partir de um palpite inicial arbitrário, são aplicados e comparados dois métodos iterativos:

* 
**Método do Aclive Máximo (Steepest Ascent):** Utiliza o gradiente local da função como direção de busca, caminhando através da relação $p = \nabla f$. Devido à ortogonalidade entre as direções sucessivas de busca, este método tende a assumir uma trajetória em "ziguezague", tornando a convergência mais lenta em vales alongados.


* 
**Método dos Gradientes Conjugados (Fletcher-Reeves):** Resolve o problema do ziguezague ao exigir que as direções de busca sucessivas sejam mutuamente conjugadas. A direção é atualizada preservando uma parcela da direção anterior: $p_{k+1} = \nabla f_{k+1} + \beta_k p_k$. O parâmetro minimizador $\beta_k$ de Fletcher-Reeves é dado por $\beta_k = \frac{|\nabla f_{k+1}|^2}{|\nabla f_k|^2}$.



Ambos os métodos compartilham o mesmo esquema de busca em linha (*line search*) baseado em interpolação quadrática de três pontos para encontrar o tamanho de passo ótimo a cada iteração.

## 2. Entradas e Saídas do Programa

O script foi desenvolvido analiticamente em **Python**, construído sem o uso de bibliotecas de integração ou otimização numéricas "caixa-preta", utilizando-se apenas estruturas de matrizes e laços de repetição.

### **Entradas (Inputs)**

O programa solicita interativamente ao usuário as seguintes entradas pelo terminal:

* **Palpite Inicial ($x_0, y_0$):** Ponto de partida no plano bidimensional para iniciar as buscas. Se nenhuma coordenada for dada, o código prevê um *fallback* numérico.
* 
**Tolerância e Limite de Iterações:** Critérios de parada embutidos (ex: $\epsilon = 10^{-5}$) baseados no módulo do erro do gradiente para atestar a convergência para o ponto crítico.



### **Saídas (Outputs)**

Ao término da execução sequencial de ambas as estratégias, o programa gera:

* 
`output1.dat`: Arquivo de log contendo o histórico do método do Aclive Máximo formatado em colunas iter, erro, h, x, y, dfx, dfy.


* 
`output2.dat`: Arquivo de log contendo o histórico do método dos Gradientes Conjugados com a mesma formatação estrutural.


* 
`function.dat`: Arquivo contendo uma amostragem em malha dos pontos x, y, e f para plotagem do campo escalar.


* 
**Mapa de Curvas de Nível:** Gráfico final bidimensional renderizado exibindo as curvas de nível da função e a sobreposição visual das duas trajetórias de busca (destacando por cor e marcador a diferença direta entre as abordagens).



## 3. Estrutura do Código

1. **Definição do Sistema:** Funções puras que retornam a avaliação de $f(x,y)$ e o seu vetor gradiente $\nabla f(x,y)$.
2. 
**Busca em Linha (Interpolação):** Rotina que aplica a fórmula do vértice da parábola para calcular o passo numérico ótimo $h^*$, com *fallback* caso o denominador seja muito pequeno.


3. **Algoritmos Iterativos:** Funções modulares separadas para o Aclive Máximo e Gradientes Conjugados (FR), incluindo os laços de convergência e armazenamento matricial do histórico.
4. **Exportação e Plotagem:** Funções que escrevem os dados `.dat` requeridos e invocam a geração da análise visual das trajetórias via *matplotlib*.

## 4. Referências Bibliográficas

* **Chapra, S. C.; Canale, R. P.** *Métodos Numéricos para Engenharia*. McGrawHill, 5ª edição (2008): 1-825.


