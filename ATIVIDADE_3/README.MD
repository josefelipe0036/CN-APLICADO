# Simulação Térmica Transiente - Combustível Nuclear

[cite_start]Este repositório contém a implementação numérica da distribuição de temperatura em regime transiente no interior de um combustível sólido de reator nuclear, utilizando o método de diferenças finitas[cite: 356, 359].

## Visão Geral
[cite_start]O código resolve a equação da difusão de calor com geração interna de energia[cite: 353]:
$$\frac{\partial T}{\partial t} = \alpha \frac{\partial^2 T}{\partial x^2} + \frac{\dot{q}}{\rho C_p}$$
[cite_start]A solução é obtida através de um esquema implícito discretizado [cite: 384, 385][cite_start], resultando em um sistema linear tridiagonal resolvido via Algoritmo de Thomas[cite: 199, 201].

## Implementação
* **Linguagem:** Python 3 (sem bibliotecas externas).
* [cite_start]**Método:** Diferenças Finitas (Esquema Implícito)[cite: 394].
* [cite_start]**Solucionador:** Algoritmo de Thomas (TDMA)[cite: 199].

## Descrição da Função `thomas_algorithm(e, f, g, r)`
[cite_start]Esta função resolve sistemas lineares na forma tridiagonal $[A]\{x\} = \{b\}$ de forma otimizada em $O(n)$[cite: 200].

### Entradas (Inputs)
* `e`: Lista contendo a subdiagonal da matriz (tamanho $N$).
* `f`: Lista contendo a diagonal principal da matriz (tamanho $N$).
* `g`: Lista contendo a superdiagonal da matriz (tamanho $N$).
* `r`: Lista contendo o vetor de termos independentes (tamanho $N$).

### Passo a Passo
1. **Forward Elimination (Decomposição L.U):** Percorre os nós de $1$ a $N-1$ eliminando a subdiagonal, atualizando os coeficientes da diagonal ($f$) e o termo de fonte ($r$) .
2. **Backward Substitution:** Resolve o valor do último nó e retrocede calculando os valores dos nós anteriores através de substituição regressiva.

### Saída (Output)
* `x`: Lista contendo a solução do sistema (vetor de temperaturas no instante $t+1$).

## Instruções de Execução
1. Certifique-se de ter o Python 3 instalado.
2. Execute o script principal: `python nome_do_arquivo.py`.
3. O código gera um arquivo `resultados_temperatura.txt` contendo os dados do perfil de temperatura (Distância vs. Temperatura).
4. Utilize este arquivo para importar e gerar os gráficos em softwares como Excel ou LibreOffice Calc.

