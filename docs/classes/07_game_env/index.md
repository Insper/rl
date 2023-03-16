# Using RL in a competitive environment
    
The goal of this activity is to implement an agent to play tic-tac-toe using Q-Learning or Sarsa algorithms and show the results.

## Tic-tac-toe player

Do you remember this code? 

```python
#
# Reference: https://pettingzoo.farama.org/environments/classic/tictactoe/
#

import gymnasium as gym
from pettingzoo.classic import tictactoe_v3

def play_random_agent(agent, obs):
    x = env.action_space(agent).sample()
    while obs['action_mask'][x] != 1:
        x = env.action_space(agent).sample()
    return x

def play_my_agent(agent, obs):
    # TODO you must implement your code here
    pass

env = tictactoe_v3.env(render_mode='human')
env.reset()

not_finish = True
while not_finish:
    for agent in ['player_1','player_2']:
        observation, reward, termination, truncation, info = env.last() 
        if termination or truncation:
            not_finish = False
        else:
            if agent == 'player_1':
                action = play_random_agent(agent,observation)
            else:
                action = play_my_agent(agent,observation)
            print(f'play: ',action)
            env.step(action)

print(env.rewards)
```

The exercise today is to **implement an agent using reinforcement learning able to play tic-tac-toe and win or draw and never lose**. 

In this case, the states (*obs*) are represented by a matrix. How to transform each possible matrix configuration into a *state id*? How many states are possible? Is it possible to define a function that has a matrix as an input and generate an *id* for each state?

## Deliver

* This exercise must be done by a group of 3 students. 

* The **deadline is 03/19/2023 23:30 -0300.**

* The implementation must be delivered through *Github classroom*. This is the link [https://classroom.github.com/a/5MNmW_QO](https://classroom.github.com/a/5MNmW_QO).

* You must add everything necessary to run this project in the repository, like the README file, requirements file and code.


