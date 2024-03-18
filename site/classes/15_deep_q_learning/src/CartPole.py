import gymnasium as gym
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
from keras import Sequential
from keras.layers import Dense
from keras.activations import relu, linear
from tensorflow.keras.optimizers import Adam
from DeepQLearning import DeepQLearning
import csv

env = gym.make('CartPole-v1')
#env.seed(0)
np.random.seed(0)

print('State space: ', env.observation_space)
print('Action space: ', env.action_space)

model = Sequential()
model.add(Dense(512, activation=relu, input_dim=env.observation_space.shape[0]))
model.add(Dense(256, activation=relu))
model.add(Dense(env.action_space.n, activation=linear))
model.summary()
model.compile(loss='mse', optimizer=Adam(learning_rate=0.001))

gamma = 0.99 
epsilon = 1.0
epsilon_min = 0.01
epsilon_dec = 0.99
episodes = 200
batch_size = 64
memory = deque(maxlen=10000) #talvez usar uma memoria mais curta
max_steps = 500

DQN = DeepQLearning(env, gamma, epsilon, epsilon_min, epsilon_dec, episodes, batch_size, memory, model, max_steps)
rewards = DQN.train()

import matplotlib.pyplot as plt
plt.plot(rewards)
plt.xlabel('Episodes')
plt.ylabel('# Rewards')
plt.title('# Rewards vs Episodes')
plt.savefig("results/cartpole_DeepQLearning.jpg")     
plt.close()

with open('results/cartpole_DeepQLearning_rewards.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    episode=0
    for reward in rewards:
        writer.writerow([episode,reward])
        episode+=1

model.save('data/model_cart_pole.keras')

