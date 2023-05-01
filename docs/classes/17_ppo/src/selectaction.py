import torch, numpy as np
probs = torch.tensor([0.1,0.9])
dist = torch.distributions.Categorical(probs)
action = dist.sample()