import numpy as np
import random
from numpy import savetxt
import sys
import matplotlib.pyplot as plt

#
# Esta classe implementa o algoritmo Q-Learning.
# Você pode usar esta implementação para criar agentes para atuar em alguns ambientes do projeto Gymansyium.
#

class QLearning:

    def __init__(self, env, alpha, gamma, epsilon, epsilon_min, epsilon_dec, episodes):
        self.env = env
        self.q_table = np.zeros([env.observation_space.n, env.action_space.n])
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_dec = epsilon_dec
        self.episodes = episodes

    def select_action(self, state):
        rv = random.uniform(0, 1)
        if rv < self.epsilon:
            return self.env.action_space.sample() # Explora o espaço de ações
        return np.argmax(self.q_table[state]) # Faz uso da tabela Q

    def train(self, filename, plotFile):
        actions_per_episode = []
        for i in range(1, self.episodes+1):
            (state, _) = self.env.reset()
            rewards = 0
            done = False
            actions = 0

            while not done:
                #
                # escolher uma acao $a$ para um estado $s$
                # executar a acao $a$
                # observar a recompensa $r$ e o novo estado $s'$ 
                # Q(s,a) \leftarrow Q(s,a) + \alpha[r + \gamma \max_{A'}Q(s',A') - Q(s,a)]
                # s recebe s'
                #

                actions=actions+1
                rewards=rewards+reward

            actions_per_episode.append(actions)
            if i % 100 == 0:
                sys.stdout.write("Episodes: " + str(i) +'\r')
                sys.stdout.flush()
            
            if self.epsilon > self.epsilon_min:
                self.epsilon = self.epsilon * self.epsilon_dec

        savetxt(filename, self.q_table, delimiter=',')
        if (plotFile is not None): self.plotactions(plotFile, actions_per_episode)
        return self.q_table

    def plotactions(self, plotFile, actions_per_episode):
        plt.plot(actions_per_episode)
        plt.xlabel('Episodes')
        plt.ylabel('# Actions')
        plt.title('# Actions vs Episodes')
        plt.savefig(plotFile+".jpg")     
        plt.close()