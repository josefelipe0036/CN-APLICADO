## 1. Adimensionalização da Equação do Movimento

O objetivo desta etapa é transformar a equação diferencial dimensional em uma forma universal que dependa dos parâmetros fundamentais: o **Número de Stokes ($St$)** e o **Número de Reynolds de partícula ($Re_s$)**[cite: 137].

### A. Equação de Partida
Para um cenário com pequenos efeitos inerciais ($Re \neq 0$), a equação dimensional é dada por[cite: 135]:
$$m_p \frac{dv_z}{dt} = -6\pi\eta a v_z - \frac{9}{4}\pi\rho_f a^2 v_z^2 + \frac{4\pi a^3}{3}\Delta\rho g$$

### B. Definição das Escalas e Parâmetros
Para a adimensionalização, utilizamos as seguintes referências[cite: 42, 138]:
* **Velocidade de Stokes ($U_s$):** Velocidade terminal em baixo Reynolds.
* **Variáveis Adimensionais (*):** $v_z^* = \frac{v_z}{U_s}$ e $t^* = \frac{t U_s}{a}$.
* **Número de Reynolds de partícula:** $Re_s = \frac{\rho_f U_s a}{\eta}$.

### C. Processo Analítico
Substituindo as variáveis dimensionais pelas suas correspondentes adimensionais e simplificando os termos conforme as definições de $St$ e $Re_s$[cite: 47, 71, 137]:

1. Substituímos $v_z = v_z^* U_s$ e $dt = dt^* \frac{a}{U_s}$.
2. Dividimos a equação pelos termos de arrasto viscoso.
3. Agrupamos as constantes nos adimensionais correspondentes.

**Forma Final Adimensional:**
$$St \frac{dv_z^*}{dt^*} = 1 - v_z^* - \frac{3}{8} Re_s (v_z^*)^2$$

---

## 2. Planejamento do Algoritmo (Runge-Kutta 4)

O planejamento a seguir visa a implementação computacional do método de Runge-Kutta de quarta ordem (RK4) para resolver a EDO de sedimentação[cite: 128, 140].

### A. Definição da Função de Evolução
A derivada temporal da velocidade é definida como[cite: 127]:
$$f(t^*, v_z^*) = \frac{1}{St} \left( 1 - v_z^* - \frac{3}{8} Re_s (v_z^*)^2 \right)$$

### B. Estrutura do Algoritmo (Fluxo Lógico)

Conforme os requisitos da atividade[cite: 141, 148]:

1. **Definição de Variáveis:**
   - Parâmetros: `St`, `Res`.
   - Numéricos: Passo de tempo `h`, tempo total de simulação.
   - Estado: `v = 0` (condição inicial de repouso)[cite: 48].

2. **Cálculo dos Coeficientes $k$ (RK4):**
   Para cada iteração temporal[cite: 131]:
   - $k_1 = f(t_i, v_i)$
   - $k_2 = f(t_i + \frac{h}{2}, v_i + \frac{h}{2}k_1)$
   - $k_3 = f(t_i + \frac{h}{2}, v_i + \frac{h}{2}k_2)$
   - $k_4 = f(t_i + h, v_i + hk_3)$

3. **Avanço Temporal:**
   - Atualizar velocidade: $v_{i+1} = v_i + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$[cite: 130].
   - Incrementar tempo: $t_{i+1} = t_i + h$.

4. **Armazenamento e Saída:**
   - Os resultados serão armazenados em vetores para geração de gráficos e comparação com as soluções analíticas de Stokes e Ricatti fornecidas[cite: 49, 79, 147].

---

### Referências
1. Sobral, Y. D., et al. (2007) [cite: 170].
2. Chapra, S. C., Canale, R. P. (2008)[cite: 171].
