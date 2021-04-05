from puzzle import Sudoku
from dqn import Agent
import numpy as np
from utils import plotLearning

env = Sudoku()
lr = 0.0005
n_games = 1
agent = Agent(gamma=0.99, epsilon=1.0, alpha=lr, input_dims=2,
                n_actions=13, mem_size=1000000, batch_size=64, epsilon_end=0.01)

# agent.load_model()
scores = []
eps_history = []


for i in range(n_games):
    done = False
    score = 0
    observation = np.array(env.reset())
    while not done:
        env.render()
        action = agent.choose_action(observation)
        observation_, reward, done = env.step(action)
        # print('Action : ',action)
        print('Reward : ',reward)
        observation_ = np.array(observation_)
        score += reward
        agent.remember(observation, action, reward, observation_, int(done))
        observation = observation_
        agent.learn()

#     eps_history.append(agent.epsilon)
#     scores.append(score)

#     avg_score = np.mean(scores[max(0, i-100):(i+1)])
#     print('episode: ', i,'score: %.2f' % score,
#             ' average score %.2f' % avg_score)

#     if i % 10 == 0 and i > 0:
#         agent.save_model()

# filename = 'lunarlander.png'

# x = [i+1 for i in range(n_games)]
# plotLearning(x, scores, eps_history, filename)