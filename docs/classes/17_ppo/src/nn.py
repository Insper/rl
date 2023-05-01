env = gym.make('CartPole-v1')

nn = torch.nn.Sequential(
        torch.nn.Linear(8,128),
        torch.nn.ReLU(),
        torch.nn.Linear(128, env.action_space.n),
        torch.nn.Softmax(dim=-1)
    )
    
# usa o Adam algorithm para otimizacao
optim = torch.optim.Adam(nn.parameters(), lr=lr)