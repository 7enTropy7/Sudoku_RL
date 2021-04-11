import neat
from puzzle import Sudoku
import os
import numpy as np

env = Sudoku()

def run(config_path):
    config = neat.config.Config(neat.DefaultGenome,neat.DefaultReproduction,neat.DefaultSpeciesSet,neat.DefaultStagnation,config_path)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    winner = p.run(main,2500000)

def main(genomes,config):
    env.reset()

    for genome_id,genome in genomes:
        genome.fitness = 0.0

    step = 0        
    
    for counter in range(9):
        ovr_id = [i for i in range(1,10)]
        t_id = 0
        for genome_id,genome in genomes:
            
            net = neat.nn.FeedForwardNetwork.create(genome,config)

            flat_observation = np.array([counter,step])
            action = net.activate(flat_observation)
            step = action.index(max(action)) + 1
            print(t_id,genome_id)
            reward, done = env.step(step,ovr_id[t_id%9]-1,counter)#(genome_id-1)%9,counter)
            # print(reward,done)
            genome.fitness += reward
            
            t_id += 1
            print("Genome : {}  Fitness : {}".format(genome_id,genome.fitness))


        env.render()

if __name__=="__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir,'config-feedforward.txt')
    run(config_path)