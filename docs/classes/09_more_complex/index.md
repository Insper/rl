# Implementando um agente para lidar com um ambiente um pouco mais complexo

Até este momento, trabalhamos com diversos ambientes que tem uma quantidade razoavelmente pequena de estados e ações discretas. O objetivo deste exercício é mostrar o uso de um método tabular (Q-Learning ou Sarsa) em um cenário onde é necessário discretizar o espaço de estados. 

Para isto, vamos utilizar o ambiente [MountainCar-v0](https://gymnasium.farama.org/environments/classic_control/mountain_car/) da biblioteca Gymnasium. Neste ambiente temos que aprender a controlar um carro que precisar sair da base de uma montanha e chegar no topo da mesma.

<img src="mountain_car.gif" alt="Mountain car environment" width="300"/>

As ações do agente são discretas: 

* 0: acelera para a esquerda.
* 1: não acelera.
* 2: acelera para a direita. 

Dado uma ação, o carro se move segundo esta dinâmica: 

$velocity_{t+1} = velocity_{t} + (action - 1) * force - cos(3 * position_{t}) * gravity$

$position_{t+1} = position_{t} + velocity_{t+1}$

onde $force = 0.001$ e $gravity = 0.0025$. 

## Entendendo o ambiente

Considere o código abaixo: 

```python
import gymnasium as gym

env = gym.make('MountainCar-v0')
(state,_) = env.reset()

print('State space: ', env.observation_space)
print('Action space: ', env.action_space)

print(env.observation_space.low)
print(env.observation_space.high)
```

Ao executar o código acima, você irá ver que a variável `state` é um vetor com duas posições. O primeiro elemento é a posição do carro e o segundo é a velocidade do carro: 

```python
array([-0.46128714,  0.        ], dtype=float32)
```

Você também verá que o espaço de estados é um espaço contínuo e que as ações são discretas.

O ambiente também tem um limite inferior e superior para o espaço de estados: 

```python
[-1.2  -0.07]
[0.6  0.07]
```

## Discretizando o espaço de estados

Uma abordagem possível para treinar um agente usando os algoritmos vistos até agora seria **discretizar o espaço de estados** e usar uma Q-table de três dimensões: posição do carro, velocidade do carro e ação.

Ao executar o código abaixo, você verá que o espaço de estados é discretizado em 19x15: 

```python
num_states = (env.observation_space.high - env.observation_space.low)*np.array([10, 100])
num_states = np.round(num_states, 0).astype(int) + 1
```

Incluindo as ações então temos uma Q-table de dimensões 19x15x3. A transformação do estado acontece da seguinte forma: 

```python
(state,_) = env.reset()
state_adj = (state - env.observation_space.low)*np.array([10, 100])
state_adj = np.round(state_adj, 0).astype(int)
```

## Treinando o agente

Para lidar com este ambiente, mesmo discretizando o espaço de estados, é necessário fazer algumas modificações no código do Q-Learning ou Sarsa.

### Na inicialização da Q-table 

```python
def __init__(self, env, alpha, gamma, epsilon, epsilon_min, epsilon_dec, episodes):

    self.env = env

    # discretizando o espaco de estados
    self.num_states = (env.observation_space.high - env.observation_space.low)*np.array([10, 100])
    self.num_states = np.round(self.num_states, 0).astype(int) + 1

    #inicializando uma q-table com 3 dimensoes: x, velocidade, acao
    self.Q = np.zeros([self.num_states[0], self.num_states[1], env.action_space.n])
```

### Na escolha da ação

```python
def select_action(self, state_adj):
    if np.random.random() < 1 - self.epsilon:
        return np.argmax(self.Q[state_adj[0], state_adj[1]]) 
    return np.random.randint(0, self.env.action_space.n)
```

### Ao manipular o estado

Podemos definir uma função: 

```python
def transform_state(self, state):
    state_adj = (state - self.env.observation_space.low)*np.array([10, 100])
    return np.round(state_adj, 0).astype(int)
```

Para então ser utilizada nas seguintes situações: 

```python
(state,_) = self.env.reset()
state_adj = self.transform_state(state)
```

e 

```python
action = self.select_action(state_adj)
next_state, reward, done, truncated, _ = self.env.step(action) 
next_state_adj = self.transform_state(next_state)
```

<!--A implementação completa desta nova versão do algoritmo Q-Learning está disponível [aqui](./src/QLearningBox.py).

## Conectando o ambiente com o treinamento do agente

Para treinar o agente e avaliar os resultados o procedimento é o mesmo que foi feito anteriormente em outros casos. Um exemplo de código que faz isto é o seguinte:  

```python
import gymnasium as gym
import numpy as np
import matplotlib.pyplot as plt
from QLearningBox import QLearningBox

env = gym.make('MountainCar-v0')

print('State space: ', env.observation_space)
print('Action space: ', env.action_space)

print(env.observation_space.low)
print(env.observation_space.high)

qlearn = QLearningBox(env, alpha, gamma, epsilon, epsilon_min, epsilon_dec, episodes)
qtable = qlearn.train('data/q-table-mountain-car.csv', 'results/rewards_MountainCar-v0')

env = gym.make('MountainCar-v0', render_mode='human')
(state,_) = env.reset()
done = False

while not done:
    env.render()
    state_adj = qlearn.transform_state(state)
    action = np.argmax(qtable[state_adj[0], state_adj[1]])
    state2, reward, done, truncated, _ = env.step(action)
    state = state2

input("enter a key...")
env.close()
```

-->

## Atividade proposta

* Implemente uma versão de Q-Learning ou Sarsa que lide com o ambiente MountainCar-v0, implementando a discretização do espaço de estados definida acima. 

* Defina os valores para os hiperparâmetros.

* Execute o treinamento e observe o comportamento do agente.

* O aprendizado do agente converge rapidamente? Fica estável? 

* Que indicador é importante utilizar para avaliar se o agente está alcançando o objetivo?

* Depois de treinado, o agente consegue chegar ao topo em todas as vezes? Quantas ações em média são necessárias? 

## Atividades complementares

* Esta implementação não tem como usar a função `savetxt` do `numpy` para gravar a *Q-table* porque a Q-table neste caso é 3D. Implemente uma função que permite armazenar e ler uma *Q-table* 3D. 

* Faça uma análise do aprendizado do agente mais robusta. Execute o treinamento do agente diversas vezes (por exemplo, 5 vezes) e analise a variabilidade do aprendizado.   

* Teste diferentes hiperparâmetros e analise o impacto no aprendizado do agente. Faça um gráfico com várias curvas de aprendizado. 

## Rubrica

| Conceito | Descrição |
|----------|-----------|
| I        | Entregou incompleto |
| C        | Implementou o agente para o ambiente Mountain Car-v0, mas não fez uma análise robusta do aprendizado |
| B        | Implementou o agente para o ambiente Mountain Car-v0 e fez uma análise robusta do aprendizado testando mais de uma configuração de hiperparâmetros |
| A+        | Implementou o agente para o ambiente Mountain Car-v0 e fez uma análise robusta do aprendizado testando mais de uma configuração de hiperparâmetros e definiu uma forma para persistência da Q-table 3D |

## Entrega

O trabalho deve ser entregue no GitHub Classroom. O link para o repositório é [https://classroom.github.com/a/DT6edFQw](https://classroom.github.com/a/DT6edFQw). O trabalho é individual. O prazo para entrega é até o dia 27/02/2025. 