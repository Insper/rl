import gymnasium as gym

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

env = make_vec_env("LunarLander-v2", n_envs=1)

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=200_000)
model.save("ppo_lunarlander")

del model

model = PPO.load("ppo_lunarlander")

print('model trained')
obs = env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()