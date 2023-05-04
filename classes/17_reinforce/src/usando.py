env = gym.make('CartPole-v1', render_mode='human')
(state, _) = env.reset()
obs = torch.tensor(state, dtype=torch.float)
done = False

while not done: 
    probs = nn(obs)
    dist = torch.distributions.Categorical(probs)
    action = dist.sample().item()
    obs_, rew, done, _, _ = env.step(action)    
    obs = torch.tensor(obs_, dtype=torch.float)