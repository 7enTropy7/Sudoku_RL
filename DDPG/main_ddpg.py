# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:27:47 2021

@author: sense
"""
from puzzle import Sudoku
import numpy as np
from agent import Agent

if __name__ == '__main__':
    env = Sudoku()
    agent = Agent(input_dims=(2,),env=env,n_actions=3)
    n_games = 1
    
    evaluate = False
    for i in range(n_games):
        observation = np.array(env.reset())
        done = False

        while not done:
            env.render()
            action = agent.choose_action(observation, evaluate)
            observation_, reward, done = env.step(action)
            print('Action : ',action)
            print('Reward ', reward)
            agent.remember(observation, action, reward, observation_, done)
            agent.learn()
            observation = observation_
            

        


        

    