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

def get_row_col_subgrid(abs_r,abs_c,sudoku):
    row = sudoku[abs_r].tolist()

    col = []
    for row in sudoku:
        col.append(row[abs_c])

    startx, starty = (abs_r//3)*3, (abs_c//3)*3
    subgrid = []
    for i in range(3):
        for j in range(3):
            subgrid.append(sudoku[startx+i][starty+j])

    dup_row,non_dup_row = num_duplicates(row)
    dup_col,non_dup_col = num_duplicates(col)
    dup_subgrid,non_dup_subgrid = num_duplicates(subgrid)

    dups = dup_row + dup_col + dup_subgrid
    non_dups = non_dup_row + non_dup_col + non_dup_subgrid

    punisher_factor = -1
    reward_factor = 0.3
    # print('Overall Reward Checking',punisher_factor * dups)
    return punisher_factor * dups + reward_factor * non_dups


class Sudoku():
    def __init__(self):
        self.puzzle = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
        self.sudoku = generate_puzzle(self.puzzle)
        # self.original_problem = generate_puzzle(self.puzzle)
        self.target = generate_puzzle('864371259325849761971265843436192587198657432257483916689734125713528694542916378')
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
        self.sudoku = generate_puzzle(self.puzzle)


    def step(self,action,id,counter):
        if counter == 8:
            self.done = True

        location = counter
        value = action
        row = (id//3)*3
        col = (id%3)*3
        abs_r = row + location//3
        abs_c = col + location%3
        if self.binary_map[abs_r][abs_c] != 1:
            self.sudoku[abs_r][abs_c] = value
            self.reward = get_row_col_subgrid(abs_r,abs_c,self.sudoku)

        return self.reward, self.done

        
    def render(self):
        # clearscreen = lambda: os.system('clear')
        # clearscreen()
        print(self.sudoku)