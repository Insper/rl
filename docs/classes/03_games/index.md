# Adversarial search and games review

## Tic-tac-toe environment and agents

Tic-tac-toe is a very simple game because it has a very small search space and in this case we usually can solve those types of problems in a manual way. Besides, this is a very good game to test very simple adversarial search algorithms. For this reason, some environments simulate this game, as [PettingZoo from Farama project](https://pettingzoo.farama.org/environments/classic/tictactoe/) or [Kaggle Environments Project](https://github.com/Kaggle/kaggle-environments).

In the code below we are using the PettingZoo project to simulate a tic-tac-toe game: 

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

def play_min_max_agent(agent, obs):
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
                action = play_random_agent(agent,observation)  # this is where you would insert your policy/algorithm
            else:
                action = play_random_agent(agent,observation) # TODO change
            print(f'play: ',action)
            env.step(action)

print(env.rewards)
```

In order to run the code above you must install those packages: 

```bash
gymnasium
IPython
matplotlib
pettingzoo
```

Please, prepare a project, with all the setup, to run the code presented above. You will see two random players playing tic-tac-toe. You must understand what is happening with the code and if you have any question, please, access the documentantion [here](https://pettingzoo.farama.org/environments/classic/tictactoe/). 

## Environments

In [class 01](../01_introduction/index.md) I asked which the main environment dimensions are. One possible answer for this question is: 

* in terms of **observations** and **actions**, there are two alternatives: **discrete** or **continuous**. The two problems (i.e., Taxi Driver and tic-tac-toe) that we saw so far are discrete in terms of observation and actions because we do not have continuous values for observations or actions.

* in terms of **dynamics**, there are two alternatives: **deterministic** or **stochastic**. In both cases, the environment is deterministic because we know the result of each action with 100% of confidence. 

* in terms of **observability**, there are also two alternatives: **full** and **partial**. We have partial observability when the agent does not have all the information necessary in each state to achieve the final goal. According to this definition, both cases are full in terms of observability. 

* in terms of **agency**, there are two alternatives: **single-agent** and **multi-agent**. If we have only our agent running in the environment then we have a single-agent environment, otherwise, we have a multi-agent environment. In terms of a multi-agent environment, we could have a competitive environment (like, tic-tac-toe, chess, go) or a collaborative environment - where the agents try to reach the same goal together. 


## Adversarial search algorithms

Adversarial search algorithms are used in competitive multi-agent environments and deterministic ones. Examples of those types of games are chess, go, shogi, tic-tac-toe and connect-4. Those games are deterministic because they do not have a stochastic movement or action. They are examples of a competitive multi-agent, deterministic, discrete and full environments. Examples of games with stochastic movements are blackjack and roulette.

The [Min-Max algorithm](https://en.wikipedia.org/wiki/Minimax) is one example of an adversarial search algorithm. We can use a Min-Max algorithm to develop agents able to play Connect-4 and Chess, for example. On [this website,](http://fbarth.net.br/Connect4-Python/) it is possible to see a full tutorial about how to create an agent able to play Connect-4 using the Min-Max algorithm.  


## Exercise: the implementation of a tic-tac-toe player using Min-Max. 

Now that we know how to implement a Min-Max algorithm, let's complete the function: 

```python
def play_min_max_agent(agent, obs):
    # TODO you must implement your code here
    pass
```

of the code below and implement an agent that can win or draw at all times. 

## Delivery

* This exercise must be done by a group of maximum 3 students. 

* The **deadline is 02/16/2023 20:00 -0300.**

* The implementation must be delivered through *Github classroom*. This is the link [](https://classroom.github.com/a/bFRDDmcO).

* You must add everything necessary to run this project in the repository, like the README file, requirements file and code.
