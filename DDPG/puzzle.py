import numpy as np
import math
import random
import os

def generate_puzzle(string):
    list1=[]
    list1[:0]=string
    for i in range(0, len(list1)):
        list1[i] = int(list1[i])
    list1 = np.array(list1)
    list1 = np.reshape(list1,(9,9))
    return list1


def num_duplicates(ls):
    c = 0
    non_duplicates = 0
    for l in ls:
        t_c = 0
        temp = [0,0,0,0,0,0,0,0,0]
        for i in l:
            if i != 0:
                temp[i-1] += 1
        
        for t in temp:
            if t > 1:
                t_c += 1
        if t_c < 1:
            non_duplicates += 1
        else:
            c += t_c
    return c,non_duplicates

def get_row_col_subgrid(sudoku):
    rows = []
    for row in sudoku:
        rows.append(row.tolist())

    cols = []
    for i in range(9):
        col = []
        for row in sudoku:
            col.append(row[i])
        cols.append(col)

    subgrids = []
    for subx in range(3):
        for suby in range(3):
            startx, starty = subx*3,suby*3
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(sudoku[startx+i][starty+j])
            subgrids.append(subgrid)

    dup_rows, non_dup_rows = num_duplicates(rows)
    dup_cols, non_dup_cols = num_duplicates(cols)
    dup_subgrids, non_dup_subgrids = num_duplicates(subgrids)

    dups = dup_rows + dup_cols + dup_subgrids
    non_dups = non_dup_rows + non_dup_cols + non_dup_subgrids

    punisher_factor = -3
    reward_factor = 1.5
    print('Overall Reward Checking',punisher_factor * dups + reward_factor * non_dups)
    return punisher_factor * dups + reward_factor * non_dups


class Sudoku():
    def __init__(self):
        self.puzzle = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
        self.sudoku = generate_puzzle(self.puzzle)
        # self.original_problem = generate_puzzle(self.puzzle)
        self.target = generate_puzzle('864371259325849761971265843436192587198657432257483916689734125713528694542916378')
        self.pos = [0,0]
        self.binary_map = generate_puzzle(self.get_binary_map())
        self.reward = 0
        self.done = False
        

    def get_binary_map(self):
        binary_map = ''
        for i in self.puzzle:
            if (i == '0'):
                binary_map += '0'
            else:
                binary_map += '1'
        return binary_map

    def reset(self):
        self.pos = [random.choice(range(9)),random.choice(range(9))]
        self.sudoku = generate_puzzle(self.puzzle)
        print('-----------------RESET---------------------')
        return self.pos


    def step(self,action):
        if (self.sudoku == self.target).all():
            self.reward = 100
            self.done = True
            
        else:
            x_n = action[0]
            y_n = action[1]
            val = action[2]+1
            
            self.pos[0] = x_n
            self.pos[1] = y_n

            if self.binary_map[x_n][y_n] == 0:
                if self.sudoku[x_n][y_n] != val:
                    self.sudoku[x_n][y_n] = val
                    # Checking for occurence in row,col,subgrid
                    self.reward = get_row_col_subgrid(self.sudoku)
             
            num_0 = 0
            for r in self.sudoku:
                num_0 += r.tolist().count(0)
            zero_reward = 5*((81-num_0)/81 - 0.43-0.2)
            self.reward += zero_reward
            print('Percentage Filled : ',100*(81-num_0)/81)

        return np.array(self.pos),self.reward,self.done    

    def render(self):
        clearscreen = lambda: os.system('clear')
        clearscreen()
        print(self.sudoku)

