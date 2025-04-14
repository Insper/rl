import gymnasium as gym
from stable_baselines3.common.torch_layers import BaseFeaturesExtractor
from torch import nn
import torch

class MinigridFeaturesExtractor(BaseFeaturesExtractor):
    def __init__(self, observation_space: gym.Space, features_dim: int = 512, normalized_image: bool = False) -> None:
        super().__init__(observation_space, features_dim)
        n_input_channels = observation_space.shape[0]
        self.cnn = nn.Sequential(
            nn.Conv2d(n_input_channels, 16, (2, 2)),
            nn.ReLU(),
            nn.Conv2d(16, 32, (2, 2)),
            nn.ReLU(),
            nn.Conv2d(32, 64, (2, 2)),
            nn.ReLU(),
            nn.Flatten(),
        )

        # Compute shape by doing one forward pass
        with torch.no_grad():
            n_flatten = self.cnn(torch.as_tensor(observation_space.sample()[None]).float()).shape[1]

        self.linear = nn.Sequential(nn.Linear(n_flatten, features_dim), nn.ReLU())

    def forward(self, observations: torch.Tensor) -> torch.Tensor:
        return self.linear(self.cnn(observations))
    
import minigrid
from minigrid.wrappers import ImgObsWrapper
from stable_baselines3 import PPO
from stable_baselines3.common.logger import configure
import sys

train = True
env_name = sys.argv[1] if len(sys.argv) > 1 else 'MiniGrid-Empty-16x16-v0'

if train:

    policy_kwargs = dict(
        features_extractor_class=MinigridFeaturesExtractor,
        features_extractor_kwargs=dict(features_dim=128), 
    )

    env = gym.make(env_name, render_mode="rgb_array")
    env = ImgObsWrapper(env)

    tmp_path = "./results/ppo-"+env_name
    new_logger = configure(tmp_path, ["stdout", "csv", "tensorboard"])

    model = PPO("CnnPolicy", env, policy_kwargs=policy_kwargs, verbose=1)
    model.set_logger(new_logger)

    model.learn(5e5)
    model.save("data/ppo-"+env_name)

    del model # remove to demonstrate saving and loading

model = PPO.load("data/ppo-"+env_name)

print('model trained')

env = gym.make(env_name, render_mode="human")
obs, _ = env.reset()
done = False

while not done:
    action, _states = model.predict(obs['image'], deterministic=True)
    obs, rewards, done, truncatee, info = env.step(action)
    env.render()



