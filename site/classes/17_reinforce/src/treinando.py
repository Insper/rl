env = gym.make('CartPole-v1')
lr = 0.0001
y = 0.999
nn, statistics = train(env, y, lr, 1200)
torch.save(nn, 'data/nn.pt')
cl = ['episode','actions','rewards']
df = pd.DataFrame(statistics, columns = cl)
df.to_csv('results/statistics_cartpole.csv')