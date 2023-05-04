torch.load('data/nn.pt')
env = gym.make('CartPole-v1', render_mode='human')
(state, _) = env.reset()
obs = torch.tensor(state, dtype=torch.float)
done = False

while not done: 
    probs = nn(obs)
    dist = torch.distributions.Categorical(probs)
    ac = dist.sample().item()
    obs_, rew, done, truncated, _info = env.step(ac)    
    obs = torch.tensor(obs_, dtype=torch.float)

