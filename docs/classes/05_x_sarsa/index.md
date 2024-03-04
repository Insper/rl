# Algoritmo SARSA: abordagem on-policy
    
## Definição e conceitos-chave

A atualização da *Q-table* no algoritmo **Q-Learning** é dada por:

$$
Q(s,a) \leftarrow Q(s,a) + \alpha [r +\gamma \max_{A'}{Q(s', A')} - Q(s,a)]
$$

A diferença entre a nova amostra e a estimativa antiga é usada para atualizar a estimativa antiga. O algoritmo **Q-Learning** considera o valor da nova amostra como o valor máximo possível de $Q$ no estado $s'$: 

$$
\max_{A'}{Q(s', A')}
$$

No entanto, a ação com o valor máximo possível de $Q$ pode não ser a ação real que o agente tomará no futuro, porque com probabilidade $\epsilon$ o agente poderá executar uma ação aleatória. Em outras palavras, a ação usada para atualizar a política em **Q-Learning** é diferente da ação real que o agente tomará. Esta é a razão pela qual **Q-Learning** é chamado de algoritmo **off-policy**. 

Por outro lado, o algoritmo **SARSA** é **on-policy** porque ele atualiza a *Q-table* com:

$$
Q(s,a) \leftarrow Q(s,a) + \alpha [r +\gamma Q(s', a') - Q(s,a)]
$$

esta equação atualiza $Q(s,a)$ considerando a ação real executada pelo agente.

O algoritmo Sarsa é muito semelhante ao algoritmo Q-Learning:

<img src="figures/sarsa.png" alt="Sarsa algorithm" style="height: 400px;"/>

## Implementação

O objetivo desta atividade é validar o entendimento do algoritmo **Sarsa** e compreender as diferenças práticas entre **Sarsa** e **Q-Learning**.

Siga os passos a seguir:

* **implementar o algoritmo Sarsa**: você pode começar a partir do arquivo `QLearning.py`, fazer uma cópia, mudar o nome :smiley:, e mudar o que for necessário.
* **aplicar a implementação do Sarsa para resolver o problema do taxi-driver**:  compare os resultados do Sarsa com os resultados do Q-Learning. Compare a curva de treinamento e o comportamento do agente após o treinamento. Você pode usar o mesmo arquivo `TaxiDriverGym.py`, mas lembre-se de mudar os nomes dos arquivos de saída (*.csv e plot). Para facilitar esta comparação, você pode usar o mesmo valor de $\epsilon$, $\alpha$ e $\gamma$ para ambos os algoritmos.
* a terceira atividade desta implementação é **aplicar os algoritmos Q-Learning e Sarsa em um ambiente diferente**: o [Cliff Walking](https://gymnasium.farama.org/environments/toy_text/cliff_walking/). Este é um ambiente muito simples. No entanto, quando você aplica esses algoritmos nesse tipo de ambiente, você pode ver as diferenças entre esses algoritmos e identificar qualquer bug em sua implementação, se existir.

Para treinar seu agente para o problema do **Cliff Walking**, você deve configurar o ambiente assim:

```python
env = gym.make("CliffWalking-v0").env
```

Depois da etapa de treinamento, para ver o comportamento, você deve codificar algo assim:

```python
env = gym.make("CliffWalking-v0", render_mode="human").env

(state, _) = env.reset()
rewards = 0
actions = 0
done = False
    
while not done:
    print(state)
    action = np.argmax(q_table[state])
    state, reward, done, truncated, info = env.step(action)

    rewards = rewards + reward
    actions = actions + 1

print("\n")
print("Actions taken: {}".format(actions))
print("Rewards: {}".format(rewards))
```

Configure o `render_mode` para `human` para ver a animação do agente.

Crie um arquivo `README.md` e responda as seguintes perguntas:

1. Qual algoritmo tem os melhores resultados para o ambiente do taxi-driver? A curva de aprendizado dos dois algoritmos é a mesma? O comportamento final do agente, depois de treinado, é ótimo? 

2. Qual algoritmo tem os melhores resultados para o ambiente do Cliff Walking? A curva de aprendizado dos dois algoritmos é a mesma? O comportamento final do agente, depois de treinado, é ótimo? Qual agente tem um comportamento mais conservador e qual tem um comportamento mais otimista?

??? hint "Sugestão para plotar a curva de aprendizado"
    Você pode usar o código a seguir para plotar a curva de aprendizado. Desta forma você irá suavisar a curva e facilitar a comparação entre os algoritmos.
    ```python
    import matplotlib.pyplot as plt

    # Calculate the rolling average of 50 values for both series
    sarsa_avg = sarsa[0].rolling(window=50).mean()
    qlearning_avg = qlearning[0].rolling(window=50).mean()

    # Plotting the rolling average series
    plt.plot(sarsa_avg, label='SARSA')
    plt.plot(qlearning_avg, label='Q-Learning')

    # Adding labels and title
    plt.xlabel('Episode')
    plt.ylabel('Reward')
    plt.title('SARSA vs Q-Learning')

    # Adding legend
    plt.legend()

    # Displaying the plot
    plt.show()
    ```

3. Suponha uma seleção de ação gulosa (*greedy*) 

```python
(
    alpha=0.1, 
    gamma=0.99, 
    epsilon=0.1, 
    epsilon_min=0.1, 
    epsilon_dec=1, 
    episodes=500
)
```
, qual seria a diferença entre os algoritmos **Q-Learning** e **Sarsa**? Os agentes treinados teriam o mesmo comportamento? As curvas de aprendizado também? 


## Rubrica de avaliação

| Conceito | Descrição |
|:---------|:----------|
| A+       | Responderam todas as perguntas e utilizaram as curvas de aprendizado e ilustrações do comportamento dos agentes treinados como base para as respostas.|
| B        | Responderam todas as perguntas e utilizaram as curvas de aprendizado como base para as respostas. |
| C        | A implementação dos algoritmos está correta, mas o estudante não entregou o arquivo README.md com as respostas. |
| D        | A implementação dos algoritmos *Q-Learning* e *Sarsa* foi parcial. |


## Entrega

Coloque todos os arquivos em um mesmo projeto e submeta-os para o [https://classroom.github.com/a/hAhU4zU3](https://classroom.github.com/a/hAhU4zU3). Esta atividade é individual e o **prazo é 05/03/2024 23:30.**

<!-- usar este texto https://www.baeldung.com/cs/q-learning-vs-sarsa para comentar os resultados do cliff walking e as diferencas entre os algoritmos -->
<!-- usar o próprio livro do Sutton para comentar os resultados -->
