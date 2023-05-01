(state, _) = env.reset()
obs = torch.tensor(state, dtype=torch.float)
done = False
Actions, States, Rewards = [], [], []

while not done:
    probs = nn(obs)
    dist = torch.distributions.Categorical(probs)
    action = dist.sample().item()
    obs_, rew, done, truncated, _ = env.step(action)

    Actions.append(torch.tensor(action, dtype=torch.int))
    States.append(obs)
    Rewards.append(rew)

    obs = torch.tensor(obs_, dtype=torch.float)
