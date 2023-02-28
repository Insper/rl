# SARSA Algorithm: on-policy approach
    
## Definition and key concepts

The updating rule in **Q-Learning** is as follows:

$$
Q(s,a) \leftarrow Q(s,a) + \alpha [r +\gamma \max_{A'}{Q(s', A')} - Q(s,a)]
$$

The difference between the new sample and the old estimation is used to update the old estimation. The **Q-Learning** algorithm considers the value of the new sample as the maximum $Q$ possible value in state $s'$: 

$$
\max_{A'}{Q(s', A')}
$$

However, the action with maximum $Q$ possible value may not be the actual action the agent will take in the future because with $\epsilon$ probability the agent will take a random action. In other words, the action used to update policy in **Q-Learning** is different from the true action the agent will take. This is the reason why **Q-Learning** is called a **off-policy** algorithm. 

On the other hand, the State-Action-Reward-State-Action (**SARSA**) algorithm is **on-policy** because it updates the Q-table with:

$$
Q(s,a) \leftarrow Q(s,a) + \alpha [r +\gamma Q(s', a) - Q(s,a)]
$$

it updates $Q(s,a)$ considering the real action executed by the agent. 

The Sarsa algorithm is very similar to the Q-Learning algorithm. The only statement that is different is the update line: 

<img src="figures/sarsa.png" alt="Sarsa algorithm" style="height: 400px;"/>

## Implementation

* Implement the Sarsa algorithm.
* Solve the taxi-driver problem using Sarsa and compare results with Q-Learning solution.
* $\cdots$ 

