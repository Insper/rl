
from stable_baselines3 import PPO, DQN, A2C
import gymnasium as gym
from stable_baselines3.common.logger import configure
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.env_util import make_vec_env

tmp_path = "./results/mc_continuous_default/"
new_logger = configure(tmp_path, ["stdout", "csv", "tensorboard"])

env = gym.make('MountainCarContinuous-v0')
vec_env = make_vec_env("MountainCarContinuous-v0", n_envs=8)

model = PPO(policy = "MlpPolicy", env = vec_env)
model.set_logger(new_logger)

model.learn(total_timesteps=500_000)

mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)
print(f'Mean reward: {mean_reward} +/- {std_reward:.2f}')

print('modelo treinado')
env = gym.make('MountainCarContinuous-v0', render_mode='human')
(obs,_) = env.reset()
for i in range(1000):
    action, _state = model.predict(obs, deterministic=True)
    obs, reward, done, truncated, info = env.step(action)
    env.render()
    if done:
      obs = env.reset()