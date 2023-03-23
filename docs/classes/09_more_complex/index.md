# Implementing an agent to deal with an environment a little more complex

Até este momento, trabalhamos com diversos ambientes que tem uma quantidade razoavelmente pequena de estados e ações discretas. O objetivo deste exercício é mostrar o uso do Q-Learning em um cenário onde é necessário discretizar o espaço de estados. 

Para isto, vamos utilizar o ambiente [MountainCar-v0](https://gymnasium.farama.org/environments/classic_control/mountain_car/) da bibliote Gymnasium. Neste ambiente temos que aprender a controlar um carro que precisar sair da base de uma montanha e chegar no topo da mesma.

<img src="mountain_car.gif" alt="Mountain car environment" width="300"/>

As ações são discretas: 

* 0: acelera para a esquerda.
* 1: não acelera.
* 2: acelera para a direita. 

Dado uma ação, o carro se move segundo esta dinâmica: 

$velocity_{t+1} = velocity_{t} + (action - 1) * force - cos(3 * position_{t}) * gravity$

$position_{t+1} = position_{t} + velocity_{t+1}$

onde $force = 0.001$ e $gravity = 0.0025$. 

## Atividades propostas: parte 1

* Abra e execute o arquivo [MountainCar_introduction.py](https://github.com/Insper/rl_code/blob/main/src/part_05/MountainCar_introduction.py) para entender melhor o ambiente. 

* Que estrutura de dados o `(state, _) = env.reset()` retorna neste caso? O que significa `state`?

* Depois de executar:

```python
print('State space: ', env.observation_space)
print('Action space: ', env.action_space)
```

O que você pode afirmar sobre o espaço de estados e as ações? 

* O que a sequência de ações abaixo faz?

```python
num_states = (env.observation_space.high - env.observation_space.low)*np.array([10, 100])
num_states = np.round(num_states, 0).astype(int) + 1
```

* O que `state_adj` representa depois de executarmos as seguintes linhas de comando: 

```python
(state,_) = env.reset()
state_adj = (state - env.observation_space.low)*np.array([10, 100])
state_adj = np.round(state_adj, 0).astype(int)
```

## Atividades propostas: parte 2

* Abra o arquivo [QLearningBox.py](https://github.com/Insper/rl_code/blob/main/src/part_05/QLearningBox.py) e veja quais são as diferenças desta implementação com a implementação do `QLearning.py` vista até agora. 

* Execute o arquivo [MountainCar.py](https://github.com/Insper/rl_code/blob/main/src/part_05/MountainCar.py). O veículo consegue chegar no topo da montanha? O que está acontecendo? O que precisa ser alterado?

* Considere o código abaixo: 

````python
(state,_) = env.reset()
done = False

while not done:
    env.render()
    state_adj = qlearn.transform_state(state)
    action = np.argmax(qtable[state_adj[0], state_adj[1]])
    state2, reward, done, _, _ = env.step(action)
    state = state2
````

Explique o que acontece nestas duas linhas: 

````python
    state_adj = qlearn.transform_state(state)
    action = np.argmax(qtable[state_adj[0], state_adj[1]])
````

## Atividades propostas: parte 3

* Analise o gráfico gerado na pasta `results`. O aprendizado do agente converge rapidamente? Fica estável? 

* Depois de treinado, o agente consegue chegar ao topo em todas as vezes? Quantas ações em média são necessárias? 

## Atividade complementar e opcional

* Esta implementação não tem como usar a função `savetxt` do `numpy` para gravar a *Q-table* porque a Q-table neste caso é 3D. Implemente uma função que permita armazenar e ler uma *Q-table* 3D. 