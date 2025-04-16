import gymnasium as gym
import torch
import pandas as pd
import csv
import torch.nn as nn
import torch.nn.functional as F
import time

#
# O objetivo desta implementação é entender o funcionamento de uma policy network.
# Para isto será utilizado o ambiente Frozen Lake modo determinístico, que é um ambiente com poucos 
# estados possíveis.
#

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

class Rede(nn.Module):
    
    #
    # o número de nodos da camada de entrada da rede será 16.
    # por exemplo, o estado inicial do agente é o estado de número 16. o mesmo será representado da seguinte forma:
    # 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1
    # da mesma forma que o estado 1 é representado por:
    # 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    #
    # o número de nodos da camada de saída será 4, pois o agente pode:
    # 0: Move up
    # 1: Move right
    # 2: Move down
    # 3: Move left
    #
    
    def __init__(self):
        super(Rede, self).__init__()
        self.input_layer = nn.Linear(16, 32)
        self.output_layer = nn.Linear(32, 4)

    def forward(self, x):
        x = self.input_layer(x)
        x = F.relu(x)
        x = self.output_layer(x)
        m = torch.nn.Softmax(dim=-1)
        return m(x)

def select_action(model, state):
    probs = model(state)
    dist = torch.distributions.Categorical(probs)
    action = dist.sample().item()
    return action

def convert_state(state):
    state_vector = [0]*16
    state_vector[state-1] = 1
    return state_vector

def atualiza_reward(rew, done):
    if rew == 0 and done:
        return -1
    return rew

def train(env, y, lr, episodes):
    
    nn = Rede().to(DEVICE)
    optim = torch.optim.Adam(nn.parameters(), lr=lr)

    statistics = []

    for i in range(episodes+1):
        (state, _) = env.reset()
        state = convert_state(state)
        obs = torch.tensor(state, dtype=torch.float).to(DEVICE)
        done = False
        Actions, States, Rewards = [], [], []
        count_actions=0
        rewards=0

        while not done and count_actions < 100:
            action = select_action(nn, obs)
            obs_, rew, done, _, _ = env.step(action)
            rew = atualiza_reward(rew, done)
            obs_ = convert_state(obs_)

            Actions.append(torch.tensor(action, dtype=torch.int).to(DEVICE))
            States.append(obs)
            Rewards.append(rew)

            obs = torch.tensor(obs_, dtype=torch.float).to(DEVICE)
            count_actions+=1
            rewards=rewards+rew
        
        if i % 100 == 0:
            print(f'Episode = {i}, Actions = {count_actions}, Rewards = {rewards}')
            # imprime as probabilidades do estado mais proximo do estado terminal de sucesso
            # a medida que o treinamento acontece percebe-se que a probabilidade da posição 1 aumenta - move right. 
            print('probs', nn(torch.tensor([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], dtype=torch.float).to(DEVICE))) 
        
        statistics.append([i, count_actions, rewards])

        DiscountedReturns = []
        for t in range(len(Rewards)):
            G = 0.0
            for k,r in enumerate(Rewards[t:]):
                G += (y**k)*r
            DiscountedReturns.append(G)

        for State, Action, G in zip(States, Actions, DiscountedReturns):
            probs = nn(State)
            dist = torch.distributions.Categorical(probs=probs)
            log_prob = dist.log_prob(Action) # isto é igual a np.log(probs[Action])

            # importante: aqui deve ser negativo pq eh um gradient ascendent
            # GA(l) = GD(-l)
            loss = -log_prob*G

            optim.zero_grad()
            loss.backward()
            optim.step()
        
    return nn, statistics

#
# iniciando o treinamento
#
print('##### Treinando o modelo #####')

env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=False)
lr = 0.0001
y = 0.999
t_inicial = time.time()
nn, statistics = train(env, y, lr, 10_000)
t_final = time.time()
print(f'Tempo de treinamento: {t_final-t_inicial}')
torch.save(nn, './data/frozen_lake.pt')

with open('./results/frozen_lake_rewards.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    episode=0
    for [i, count_actions, rewards] in statistics:
        writer.writerow([i,rewards])
        episode+=1

#
# Depois de treinado
#
print('##### Modelo treinado #####')

#nn = torch.load('./data/frozen_lake.pt')
env = gym.make('FrozenLake-v1', desc=None, map_name="4x4", is_slippery=False, render_mode="human")
(state, _) = env.reset()
state = convert_state(state)
obs = torch.tensor(state, dtype=torch.float).to(DEVICE)
done = False

while not done: 
    action = select_action(nn, obs)
    obs_, rew, done, truncated, _info = env.step(action)    
    obs_ = convert_state(obs_)
    obs = torch.tensor(obs_, dtype=torch.float).to(DEVICE)

