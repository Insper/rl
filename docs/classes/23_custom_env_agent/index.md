# Um problema mais próximo da realidade

Na atividade no link [Custom Environment](../22_custom_env/index.md), criamos um ambiente personalizado para o problema de Coverage Path Planning. Desde a última atividade, este ambiente sofreu algumas modificações, principalmente com relação a representação do estado. Agora, o estado é representado por uma estrutura de dados mais complexa, que inclui informações sobre a posição do agente, o mapa parcial do ambiente e o progresso da cobertura. 

Leia a última seção do arquivo README.md (Uso do ambiente GridWorld para problemas de Coverage Path Planning) do projeto [https://github.com/fbarth/gym_custom_env](https://github.com/fbarth/gym_custom_env) para entender melhor as mudanças realizadas no ambiente.

Neste mesmo projeto, existe um script chamado `train_grid_world_cpp.py` que treina um agente utilizando o algoritmo PPO. 

O agente, quando treinado para o ambiente 5x5 consegue aprender a realizar a cobertura completa do ambiente, mas não é capaz de generalizar para ambientes maiores, como o 10x10. Quando o agente, que é treinado no ambiente 5x5, é testado no ambiente 10x10, ele em várias situações fica preso em alguma parte do ambiente, sem conseguir realizar a cobertura completa.

O que será que é necessário fazer para que o agente consiga generalizar melhor para ambientes maiores?

## O que falta?

* Falta algo na representação do estado? Lembrete importante: a informação sobre o ambiente é parcial, ou seja, o agente não tem acesso ao mapa completo do ambiente, apenas a um mapa parcial baseado no que ele já explorou.
* A arquitetura da rede neural utilizada no treinamento não é adequada. A arquitetura que está configurada no script `train_grid_world_cpp.py` é do tipo `MultiInputPolicy`. A documentação sobre esta arquitetura está disponível neste [link](https://stable-baselines3.readthedocs.io/en/master/guide/custom_policy.html). 
* Será que é necessário realizar alguma atividade de *transfer learning* para que o agente consiga generalizar melhor para ambientes maiores? Por exemplo, uma vez treinado no ambiente 5x5, o agente poderia ser treinado por mais algumas iterações no ambiente 10x10, utilizando o modelo treinado no ambiente 5x5 como ponto de partida. Para que isto aconteça é necessário configurar o script `train_grid_world_cpp.py` para que ele possa carregar um modelo pré-treinado e continuar o treinamento em um ambiente diferente. Isto é possível utilizando a função `load` da biblioteca Stable Baselines 3. 
* Será que os hiperparâmetros utilizados no treinamento do agente não são adequados? 
* Será que é necessário utilizar outro algoritmo de RL? 

A configuração utilizada no treinamento foi a seguinte:

```python
# --- Hyperparameters ---
DIM = 5 #10, 20
OBSTACLES = 3 #12, 48 mudanco a dimensao, faz sentido mudar a quantidade de obstaculos
MAX_STEPS = 200#400, 800 e o max_steps
TOTAL_TIMESTEPS = 1_000_000
ENTROPY_COEF = 0.05
# -----------------------

model = PPO("MultiInputPolicy", env, verbose=1, ent_coef=ENTROPY_COEF, device="cpu")
```

Ao executar: 

```bash
python train_grid_world_cpp.py test
```

Os resultados para *Full Coverage Rate* no ambiente 5x5 são:

```
75/100
78/100
69/100
79/100
81/100
```

Ou seja, mesmo para o ambiente 5x5, o agente não consegue realizar a cobertura completa em todas as execuções.

Usando o agente treinado no ambiente 5x5 para realizar a cobertura no ambiente 10x10, os resultados para *Full Coverage Rate* são:

```
66/100
65/100
60/100
70/100
59/100
```

Ou seja, o agente tem uma performance pior no ambiente 10x10 do que no ambiente 5x5, o que indica que ele não está generalizando bem para ambientes maiores.

Pode-se fazer uma análise mais qualitativa do comportamento do agente executando: 

```bash
python train_grid_world_cpp.py run
```

**O que é necessário fazer para que o agente consiga ter cobertura próxima de 100% no ambiente 5x5, 10x10 e, idealmente, em ambientes ainda maiores?**

## O que é necessário fazer?

* Faça fork ou clone do projeto [https://github.com/fbarth/gym_custom_env](https://github.com/fbarth/gym_custom_env).
* Defina uma estratégia, implemente a estratégia escolhida e teste a performance do agente no ambiente 5x5 e 10x10 no novo repositório.
* Crie um relatório descrevendo a estratégia escolhida e os resultados obtidos. O arquivo do relatório deve estar disponível no repositório do projeto. No arquivo README.md do projeto deve estar claro onde o relatório pode ser encontrado. 
* Este trabalho é individual, ou seja, cada pessoa deve criar um repositório com a sua própria solução. O prazo para entrega é **08/05/2026**. O link para o repositório deve ser enviado no blackboard até a data de entrega.
* Este trabalho vale como uma APS, mas também será contabilizado como parte da avaliação final da disciplina. **Este trabalho irá valer 2 pontos na avaliação final da disciplina**. Ou seja, se você não fizer esta APS, você irá perder 2 pontos na avaliação final da disciplina.
* O relatório deve conter uma descrição clara da estratégia escolhida, os resultados obtidos e uma análise dos resultados. A estratégia escolhida deve ser justificada com base em conceitos de RL e na estrutura do ambiente. Os resultados devem ser apresentados de forma clara, utilizando gráficos e tabelas quando necessário. A análise dos resultados deve discutir o desempenho do agente, as limitações da estratégia escolhida e possíveis melhorias para futuras implementações.
* O desempenho do agente precisa ter cobertura próxima de 100% no ambiente 5x5 e 10x10. 
* O agente precisa manter a visualização parcial do ambiente, ou seja, ele não pode ter acesso ao mapa completo do ambiente. O agente deve tomar decisões com base no mapa parcial que ele tem disponível e outras informações que ele poderá coletar ao longo do processo de exploração do ambiente.

## Ponto extra

Se a sua implementação conseguir ter cobertura próxima de 100% em ambiente 5x5, 10x10 e 20x20, você irá ganhar um ponto extra na avaliação final da disciplina.
