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

def num_duplicates(l):
    c = 0
    nd = 0
    temp = [0,0,0,0,0,0,0,0,0]
    for i in l:
        if i!=0:
            temp[i-1] += 1
    for t in temp:
        if t > 1:
            c += t-1
        if t == 1:
            nd += 1
    return c, nd

def get_row_col(abs_r,abs_c,sudoku):
    row = sudoku[abs_r].tolist()

    col = []
    for row in sudoku:
        col.append(row[abs_c])

    dup_row,non_dup_row = num_duplicates(row)
    dup_col,non_dup_col = num_duplicates(col)

    dups = dup_row + dup_col
    non_dups = non_dup_row + non_dup_col

    punisher_factor = -1
    reward_factor = 1

    return punisher_factor * dups + reward_factor * non_dups

def get_reward(genome_id):
    row = (genome_id//3)*3
    col = (genome_id%3)*3
    abs_r = row + env.last_action[genome_id]//3
    abs_c = col + env.last_action[genome_id]%3
    reward = get_row_col(abs_r,abs_c,env.sudoku)
    return reward


def main(genomes,config):
    env.reset()

    for genome_id,genome in genomes:
        genome.fitness = 0.0

    done = False
    step = 0
    for counter in range(18):
        ovr_id = [i for i in range(1,10)]
        t_id = 0
        for genome_id,genome in genomes:
            
            net = neat.nn.FeedForwardNetwork.create(genome,config)

            flat_observation = np.array(env.get_subgrid_state(ovr_id[t_id%9]-1))
            action = net.activate(flat_observation)
            step = action.index(max(action))

            env.step(step,ovr_id[t_id%9]-1)#(genome_id-1)%9,counter)
            t_id += 1

        p_id = 0
        for genome_id,genome in genomes:    
            reward = get_reward(ovr_id[p_id%9]-1)
            genome.fitness = reward
            p_id += 1
            
            print("Genome : {}  Fitness : {}".format(genome_id,genome.fitness))

        if (env.sudoku == env.target).all():
            done = True
        print(done)
        env.render()

if __name__=="__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir,'config-feedforward.txt')
    run(config_path)