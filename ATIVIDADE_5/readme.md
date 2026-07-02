# Solução Numérica da Equação de Blasius (Camada Limite Laminar)

Este repositório contém a implementação em Python para a resolução numérica da Equação de Blasius por meio de variáveis de similaridade. O código foi desenvolvido como parte da Atividade e Programa para Casa #5 (APC/PPC) da disciplina de Cálculo Numérico Aplicado da Universidade de Brasília (UnB).

O objetivo principal é converter um Problema de Valor de Contorno (PVC) em um Problema de Valor Inicial (PVI) utilizando o **Método do Tiro** acoplado ao método de integração de **Runge-Kutta de 4ª Ordem (RK4)**.

## Pré-requisitos e Dependências

O motor de integração numérica foi construído inteiramente do zero utilizando apenas as estruturas nativas do Python, sem o uso de bibliotecas de cálculo de terceiros (como `scipy.integrate`), cumprindo estritamente as exigências da atividade. 

A única biblioteca externa necessária é o `matplotlib`, utilizada exclusivamente para a plotagem dos perfis de velocidade.

Para instalar a dependência, execute no seu terminal:
`pip install matplotlib`

## Como Executar

Faça o clone deste repositório e execute o script principal:

`python blasius_solver.py`

## Parâmetros de Entrada (Inputs)

Os parâmetros numéricos necessários para a simulação estão definidos no bloco principal (`__main__`) do script. Você pode alterá-los diretamente no código caso deseje refinar a malha ou testar diferentes tolerâncias:

*   **`h`**: Passo de integração espacial (padrão atual: 0.01).
*   **`eta_max`**: Valor máximo do domínio numérico, representando o infinito físico longe da placa (padrão atual: 10.0).
*   **`tol`**: Tolerância de convergência para o Método do Tiro (padrão atual: 1e-6).
*   **`max_iter`**: Número máximo de iterações permitidas para o método da Secante atualizar os chutes (padrão atual: 100).
*   **`chute_inicial_0` e `chute_inicial_1`**: Valores arbitrários iniciais para a tensão de cisalhamento na parede (f''(0)).

## Saídas Geradas (Outputs)

Ao finalizar o processamento iterativo, o programa consolida os resultados em três frentes:

1. **Saída em Tela (Console):**
   * O valor numérico convergido para o parâmetro de tiro (f''(0)).
   * O número total de iterações realizadas pelo Método do Tiro até a convergência.
   * O erro numérico final obtido na fronteira (f'(eta_max) - 1).
   * Uma análise comparativa imprimindo os erros relativos percentuais em relação aos valores clássicos da literatura (f''(0) = 0.332057).

2. **Exportação de Dados em Arquivo:**
   * O programa gera automaticamente um arquivo chamado `resultados_blasius.txt` na mesma pasta do script.
   * Este arquivo contém os vetores populados em colunas estruturadas (eta, f, f', f''), prontos para leitura em outros softwares de pós-processamento, caso necessário.

3. **Visualização Gráfica (Plot):**
   * Uma janela interativa é aberta mostrando os perfis de similaridade da função de corrente, velocidade e tensão de cisalhamento.
   * O gráfico calcula via interpolação linear e destaca graficamente o ponto exato da espessura da camada limite, onde a velocidade atinge 99% do escoamento livre.

