# Tracking Non-Stationary Problems

## Pre-work

In the last class, we have implemented greedy and $\epsilon$-greedy algorithms for the multi-armed bandit problem. Please, check the results in this [file](bandit_answers.pdf) and try to review the code and results. If you have any questions, please, ask! 

## Non-Stationary Bandits

In the previous class, we have assumed that the reward distribution of each arm is stationary, i.e., it does not change over time. However, in many real-world applications, the reward distribution can change over time. For example, in a recommendation system, the user's preferences may change over time. In a stock trading application, the market conditions may change over time.

??? warning "Check this!"

    Check this [notebook](non_stationary_bandits.ipynb) for an implementation of a non-stationary bandit problem and a simple algorithm to track the changing rewards.

<embed src="main.pdf" type="application/pdf" width="750" height="400">
