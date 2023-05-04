import torch, numpy as np
probs = torch.tensor([0.1,0.9])
dist = torch.distributions.Categorical(probs)
action = dist.sample() # => 1

dist.log_prob(action)  # => -0.105
np.log(0.9)            # => -0.105
