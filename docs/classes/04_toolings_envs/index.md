# Reinforcement Learning Tooling and Environments

According to the [Farama Foundation](https://farama.org/), Reinforcement learning is a popular approach to AI where an agent learns to take sequential actions in an environment through trial and error. Reinforcement learning is conceptualized as a loop where the agent observes the state of its environment, and then takes an action that changes that state. At the time of receiving the next observation, the agent also receives a reward associated with the most recent action. This process continues in a cycle, and during learning the agent seeks to maximize its expected average reward. In practice, environments are most often a piece of software like a game or simulation.  

In supervised learning, the basic software stack typically only has three components: the dataset, preprocessing of the dataset, and the deep learning library. In reinforcement learning, the software stack is much more complex. It starts with constructing the environment itself, usually a piece of software like a simulation or a video game. The base environment logic is then wrapped with an API that learning code can be applied to. Depending on how the reinforcement learning algorithm interacts with the environment, preprocessing wrappers are then applied (e.g. to make image observations greyscale). Only after all of this is done can a reinforcement learning algorithm be applied. 

## Main References

1. [The Farama Foundation](https://farama.org/Announcing-The-Farama-Foundation).
1. How to use [Gymnasium API](https://gymnasium.farama.org/): a Python library for single agent reinforcement learning.
1. [PettingZoo](https://pettingzoo.farama.org/): a Python library for multi-agent reinforcement learning.
1. [SuperSuit](https://github.com/Farama-Foundation/SuperSuit): wrappers for RL environments. 

## Other tools

1. [Worldgen](https://openai.com/blog/emergent-tool-use/).
