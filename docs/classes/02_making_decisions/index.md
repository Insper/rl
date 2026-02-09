---
title: Multi-Armed Bandits
subtitle: Making Decisions Under Uncertainty
author: Fabricio Barth
date: February, 2026
---

# Multi-Armed Bandits

**Theme:** Making decisions under uncertainty (clinical trials example)

<small>Based on the ideas from *Reinforcement Learning: An Introduction* (Sutton & Barto), pp. 25–36.</small>

---

# Agenda

- Bandit problem setup <!-- .element: class="fragment" -->
- Clinical trials as a decision problem <!-- .element: class="fragment" -->
- Action-value definition and expected reward <!-- .element: class="fragment" -->
- Estimating action values <!-- .element: class="fragment" -->
- $\varepsilon$ - greedy action selection <!-- .element: class="fragment" -->

---

# The Bandit Problem

You have $k$ actions (arms). Each action $a$ produces a reward $R$ drawn from an unknown distribution.

<span class="fragment">Goal: maximize cumulative reward by balancing exploration and exploitation.</span>

---

# Clinical Trials Scenario

Imagine $k$ treatments for the same condition.

- Each patient is a trial <!-- .element: class="fragment" -->
- A treatment is an action <!-- .element: class="fragment" -->
- Observed outcome is a reward <!-- .element: class="fragment" -->
- We must learn which treatment works best <!-- .element: class="fragment" -->

---

# Notation

- $A_t$: action chosen at time $t$ <!-- .element: class="fragment" -->
- $R_t$: reward observed after choosing $A_t$ <!-- .element: class="fragment" -->
- $q_*(a)$: true value of action $a$ <!-- .element: class="fragment" -->

---

# Expected Reward of an Action

The **true action value** is the expected reward of action $a$:

$$
q_*(a) = \mathbb{E}[R_t \mid A_t = a]
$$

<span class="fragment">We do not know $q_*(a)$, so we must estimate it from data.</span>

---

# Action-Value Estimate (Sample Average)

Let $N_t(a)$ be the number of times action $a$ has been selected up to time $t$.

$$
\hat{q}_t(a) = \frac{1}{N_t(a)} \sum_{i=1}^{t} R_i \cdot \mathbb{1}\{A_i = a\}
$$

<span class="fragment">This estimate converges to $q_*(a)$ as $N_t(a)\to\infty$.</span>

---

# Incremental Update Form

Instead of storing all rewards, update online:

$$
\hat{q}_{t+1}(A_t) = \hat{q}_t(A_t) + \frac{1}{N_t(A_t)}\left(R_t - \hat{q}_t(A_t)\right)
$$

<span class="fragment">Only the selected action is updated each step.</span>

---

# Explore vs. Exploit

- **Exploit**: choose the best estimated action <!-- .element: class="fragment" -->
- **Explore**: try actions with uncertain or lower estimates <!-- .element: class="fragment" -->

<span class="fragment">Clinical trials must explore to discover better treatments, but also exploit to help current patients.</span>

---

# $\varepsilon$ - Greedy Action Selection

Choose:

- with probability $\varepsilon$, a random action (explore) <!-- .element: class="fragment" -->
- with probability $1-\varepsilon$, the greedy action (exploit) <!-- .element: class="fragment" -->

$$
A_t =
\begin{cases}
	ext{random action}, & \text{with prob. } \varepsilon \\
\arg\max_a \hat{q}_t(a), & \text{with prob. } 1-\varepsilon
\end{cases}
$$

---

# What Does $\varepsilon$ Control?

- Larger $\varepsilon$ $
ightarrow$ more exploration <!-- .element: class="fragment" -->
- Smaller $\varepsilon$ $
ightarrow$ more exploitation <!-- .element: class="fragment" -->

<span class="fragment">A common choice is $\varepsilon = 0.1$, but it depends on the problem.</span>

---

# Clinical Trials: Why $\varepsilon$ - Greedy?

- Avoids prematurely committing to a suboptimal treatment <!-- .element: class="fragment" -->
- Ensures all treatments are sampled <!-- .element: class="fragment" -->
- Simple and effective baseline method <!-- .element: class="fragment" -->

---

# Summary

- Multi-armed bandits model decision-making with uncertainty
- Action value: $q_*(a) = \mathbb{E}[R_t \mid A_t=a]$
- Estimate values via sample averages or incremental updates
- $\varepsilon$-greedy balances exploration and exploitation

---

# References

- Sutton, R. S., & Barto, A. G. *Reinforcement Learning: An Introduction*, 2nd ed., pp. 25–36.
