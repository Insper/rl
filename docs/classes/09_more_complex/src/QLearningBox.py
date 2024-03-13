import numpy as np
from numpy import savetxt
import matplotlib.pyplot as plt

class QLearningBox:

    def __init__(self, env, alpha, gamma, epsilon, epsilon_min, epsilon_dec, episodes):
        self.env = env
        # discretizando o espaco de estados
        self.num_states = (env.observation_space.high - env.observation_space.low)*np.array([10, 100])
        self.num_states = np.round(self.num_states, 0).astype(int) + 1

        #inicializando uma q-table com 3 dimensoes: x, velocidade, acao
        self.Q = np.zeros([self.num_states[0], self.num_states[1], env.action_space.n])

        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_dec = epsilon_dec
        self.episodes = episodes

    def select_action(self, state_adj):
        if np.random.random() < 1 - self.epsilon:
            return np.argmax(self.Q[state_adj[0], state_adj[1]]) 
        return np.random.randint(0, self.env.action_space.n)

    def transform_state(self, state):
        state_adj = (state - self.env.observation_space.low)*np.array([10, 100])
        return np.round(state_adj, 0).astype(int)

    def train(self, filename, plotFile=None):         
        reward_list = []
        ave_reward_list = []
        actions_per_episode = []
    
        for i in range(self.episodes):
            done = False
            tot_reward, reward = 0,0
            (state,_) = self.env.reset()
            state_adj = self.transform_state(state)
    
            qtd_actions = 0
            while done != True:   
                action = self.select_action(state_adj)
                next_state, reward, done, truncated, _ = self.env.step(action) 
                next_state_adj = self.transform_state(next_state)
            
                # atualizacao direta para estados terminais. 
                if done and next_state_adj[0] >= 0.5:
                    self.Q[state_adj[0], state_adj[1], action] = reward
                # ajustando Q-valor para estados atuais
                else:
                    delta = self.alpha*(reward + self.gamma * np.max(self.Q[next_state_adj[0], next_state_adj[1]]) - self.Q[state_adj[0], state_adj[1],action])
                    self.Q[state_adj[0], state_adj[1],action] += delta
                                     
                tot_reward += reward
                state_adj = next_state_adj
                qtd_actions = qtd_actions + 1
        
            if self.epsilon > self.epsilon_min:
                self.epsilon = self.epsilon * self.epsilon_dec
        
            reward_list.append(tot_reward)
        
            if (i+1) % 100 == 0:
                ave_reward = np.mean(reward_list)
                ave_reward_list.append(ave_reward)
                actions_per_episode.append(qtd_actions)
                reward_list = []
            
            if (i+1) % 100 == 0:    
                print('Episode {} Average Reward: {}  Actions in this episode {} '.format(i+1, ave_reward, actions_per_episode[len(actions_per_episode)-1]))

        # TODO Q eh um vetor tridimensional. savetxt nao trabalha com arrays com mais de 2
        # dimensoes. Eh necessario fazer ajustes para armazenar a Q-table neste caso.
        #savetxt(filename, self.Q, delimiter=',')
        if (plotFile is not None): self.plotactions(plotFile, ave_reward_list)
        return self.Q

    def plotactions(self, plotFile, rewards):
        plt.plot(100*(np.arange(len(rewards)) + 1), rewards)
        plt.xlabel('Episodes')
        plt.ylabel('Average Reward')
        plt.title('Average Reward vs Episodes')
        plt.savefig(plotFile+".jpg")     
        plt.close() 