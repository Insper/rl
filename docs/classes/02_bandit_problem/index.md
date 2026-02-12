# The Bandit Problem

The goal of this class is to introduce the **multi-armed bandit problem** as a fundamental model for **decision-making under uncertainty**, and to show how it captures the core ideas behind reinforcement learning.

In this class, we aim to:

- Understand how repeated decisions with uncertain outcomes can be formally modeled
- Learn how to **estimate the value of actions** from noisy reward observations
- Explore the central **exploration vs. exploitation trade-off**
- Study simple and effective decision strategies, such as **ε-greedy action selection**
- Connect theoretical concepts to **real-world scenarios**, including clinical trials and everyday choices

By the end of the class, students should be able to:

- Formulate a problem as a multi-armed bandit
- Explain why exploration is necessary for learning
- Describe how ε-greedy strategies balance learning and performance in practice

<embed src="main.pdf" type="application/pdf" width="600" height="300">

## Exercises

During the explanation of the bandit problem, we will work through several exercises to solidify our understanding. These exercises are available in the [bandit.ipynb](code/bandit.ipynb) notebook, which you can download and run locally. We also provide a [requirements.txt](code/requirements.txt) file to help you set up the necessary Python environment.

## References

* Sutton, R. S., & Barto, A. G. (2018). Reinforcement learning: An introduction. MIT press, pages 25-36.
* Arm Bandit environment [https://github.com/foreverska/buffalo-gym](https://github.com/foreverska/buffalo-gym).


