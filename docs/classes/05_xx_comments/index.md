# Comments about Q-Learning and Sarsa implementation 

*Answers from Carlos Dip, André Tavernaro and Letícia.*

* Which algorithm has the best results for the taxi-driver environment? 

In my implementation, the SARSA algorithm converged slightly faster than Q-Learning. In simulations, they seemed to perform similarly, with no big differences in pathing.

* Which algorithm has the best results for the Cliff Walking environment? 

In my implementation, the QLearning algorithm converged a bit faster than SARSA. In the simulation, there was a big difference in behavior. Since SARSA learns while taking into account random actions, it tries to steer clear of the cliff in this scenario. This happens because, during its training, there was a random chance it would fall despite it being a known bad action. This means the Q-Table essentially learns to be sacred of costly mistakes.

* Try to explain the results. Why one algorithm is better than another? 

It seems like SARSA is more interesting when you are looking for a risk-minimizing strategy. It is more careful and looks into making less strictly efficient decisions preferring to minimize risks. Q-Learning, on the other hand, is much more direct. It maximizes rewards, regardless of risks. I would not say either algorithm is better, they are just more suited to certain situations. In a non-deterministic environment, this risk-averse behavior might be more interesting, although perhaps a hybrid of risk aversion and pure efficiency.

* Do a small research about Sarsa algorithm to understand its cons and pros. 

SARSA is an example of an on-policy Reinforcement Learning algorithm. This means that the policy it follows during learning is the same as the one it uses to update its policy. In this case, we use an epsilon-greedy policy, meaning we take the best-known option, with an epsilon randomness factor chance of taking a random action instead. This means SARSA learns a near-optimal policy instead of an optimal one, which can be bad if a problem requires the optimal solution. Since SARSA tends to avoid mistakes while training, it is more advantageous to use it in scenarios where these mistakes are costly, such as training using real-world data, like a robot or self-driving car.

Q-Learning in the Cliff walking world:

<img src="figures/QLearning-Cliff.png" alt="Q-Learning in the Cliff walking world" style="height: 200px;"/>

Sarsa in the Cliff walking world:

<img src="figures/Sarsa-Cliff.png" alt="Sarsa in the Cliff walking world" style="height: 200px;"/>

## QLearning vs  Sarsa - Vantagens e Desvantagens 📌️ 

- `QLearning`

$$Q(S_t, A_t) = Q(S_t, A_t) + \alpha[R_{t+1} + \gamma max(Q(S_{t+1}, a)) - Q(S_t, A_t) ]$$

Algorítimo que busca encontrar a melhor ação a ser tomada, dado um estado atual. 

É considerao um algoríitmo **off-policy**, pois a melhor ação é escolhida para a atualização da **q_table** mesmo que essa ação não seja aplicada nessa ocasião (fator de aleatoriedade na tomada de uma ação - **Explore**).

Como o QLearning aprende com a "política ótima", ele é considerado um algorítimo mais "agressivo. Ou seja, No exemplo do ambiente CliffWalking o QL seguirá o caminho mais curto, pois esse é o caminho ótimo, mesmo que haja risco maior de queda.

- `Sarsa`

$$Q(S_t, A_t) = Q(S_t, A_t) + \alpha[R_{t+1} + \gamma Q(S_{t+1}, A_{t+1}) - Q(S_t, A_t) ]$$

Como é possível observar pela formula, o algorítimo SARSA aprende com uma política "quase ótima". Um agente treinado com o algorítimo SARSA interage com o ambiente atualizando **q_table** com base nas ações efetivamente tomadas. Quando o problema envolve achar a solução ótima ou quando o número mínimo de ações deve ser tomada na resolução do problema, o algorítimo SARSA pode não se apresentar como a melhor escolha.

## Valores utilizados com mais frequência

```python
sarsa = Sarsa(env, alpha=0.1, gamma=0.99, epsilon=0.7, epsilon_min=0.1, epsilon_dec=0.99999, episodes=10000)
```

Alguém testou?

```python
sarsa = Sarsa(env, alpha=0.1, gamma=0.99, epsilon=0, epsilon_min=0, epsilon_dec=0.99999, episodes=10000)
```

o que acontece? 

