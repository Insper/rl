# Ambientes não-determinísticos
    
O ambiente [Frozen Lake](https://gymnasium.farama.org/environments/toy_text/frozen_lake/) é um ambiente não determinístico onde um agente deve encontrar um caminho do lugar onde ele está para outro lugar passando por buracos. Se ele chegar no objetivo sem cair no buraco então ele termina a tarefa e tem 1 ponto de reward. Se ele cair em um dos buracos então ele termina a tarefa com 0 pontos de reward. Cada ação que não leva para um estado terminal tem reward igual a 0.  

Neste ambiente o agente consegue executar 4 ações: ir para cima, ir para baixo, ir para esquerda e ir para direita. **Como o chão é de gelo, não necessariamente a ação de ir para baixo vai levar o agente para baixo**, por exemplo. Isto acontece com todas as quatro ações. Por isso que este ambiente é não determinístico.

O ambiente Frozen Lake está disponível no pacote `gymnasium` com duas configurações: 4x4 e 8x8. 

```python
import gymnasium as gym
env = gym.make('FrozenLake-v1', map_name="4x4", is_slippery=True).env
env = gym.make("FrozenLake-v1", map_name="8x8", is_slippery=True).env
```

A função de recompensa é dada por: 


\begin{equation}
R(s_{i}, A) = \begin{cases}
    1, & \text{se } s_{i} = \text{objetivo} \\
    0, & \text{se } s_{i} = \text{buraco} \\
    0, & \text{caso contrário}
    \end{cases}
\end{equation}

Os estados terminais são o objetivo e os buracos. Mas se o agente fizer mais de 100 movimentos no ambiente $4 \times 4$ ou mais de 200 movimentos no ambiente $8 \times 8$ então o episódio termina com `truncated` igual a `True`.

## Perguntas

* É possível treinar um agente capaz de atuar no ambiente do Frozen Lake? Ou seja, é possível treinar um agente capaz de atuar em um mundo **não-determinístico**?

* Qual é o melhor algoritmo e os melhores hiperparâmetros para treinar um agente capaz de atuar no ambiente do Frozen Lake?

## Método

Para responder as perguntas acima você deve treinar um agente capaz de atuar no ambiente do Frozen Lake e comparar a curva de aprendizagem do agente treinado com a curva de aprendizagem de outros agentes treinados com diferentes algoritmos e hiperparâmetros. 

Você deve treinar o agente com os algoritmos Q-Learning e SARSA escolhendo uma configuração de hiperparâmetro que deve ser aplicada em ambos os algoritmos. Ou seja, você irá comparar a curva de aprendizagem de 2 agentes diferentes. Nesta atividade considere apenas o ambiente $4 \times 4$.

<!-- **Detalhe importante**: neste ambiente o reward é apenas 0 ou 1. Sendo assim, se você utilizar uma abordagem de medida como a exercitada na [aula anterior](../11_evaluation/index.md#exercício-comparar-q-learning-e-sarsa-no-ambiente-do-cliff-walking) provavelmente você não vai conseguir comparar os algoritmos. Nesta caso, a melhor abordagem é comparar a curva de aprendizagem dos agentes treinados usando uma média móvel dos rewards obtidos ao longo do treinamento.-->

Após treinar os agentes você deve utilizar o agente com melhor desempenho e executar 100 vezes no ambiente $4 \times 4$ e calcular a quantidade de vezes que o agente chegou até o destino final sem cair no buraco.

## Artefatos que devem ser entregues

Cada aluno deve entregar os seguintes artefatos: 

* Relatório com os gráficos das curvas de aprendizado dos agentes treinados e dados sobre o desempenho do melhor agente no ambiente (quantidade de vezes que o agente chegou até o destino final sem cair no buraco).

* Todos os códigos utilizados para executar os experimentos.

* Arquivo README.md descrevendo como executar o experimento. 

A entrega deve ser feita através do [https://classroom.github.com/a/fayO19QB](https://classroom.github.com/a/fayO19QB). O trabalho é individual.

### Rubrica de avaliação

* O relatório deve conter uma descrição detalhada dos experimentos realizados e uma discussão sobre os resultados obtidos.

* O código deve estar bem organizado e documentado.

* O README.md deve conter instruções claras sobre como executar o experimento.

### Prazo de entrega

O prazo para a entrega desta atividade é 25 de fevereiro de 2025. 