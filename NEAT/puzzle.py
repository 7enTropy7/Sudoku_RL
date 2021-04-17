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


def get_subgrids(sudoku):
    subgrids = []
    for subx in range(3):
        for suby in range(3):
            startx, starty = subx*3,suby*3
            subgrid = []
            for i in range(3):
                for j in range(3):
                    subgrid.append(sudoku[startx+i][starty+j])
            subgrids.append(subgrid)
    return subgrids 

def return_initialized_puzzle(sudoku):
    subgrids = get_subgrids(sudoku)
    t = [9,8,7,6,5,4,3,2,1]
    for subgrid in subgrids:
        temp = []
        output_grid = []
        for i in range(len(subgrid)):
            if subgrid[i] != 0:
                temp.append(subgrid[i])
        for i in t:
            if i not in temp:
                output_grid.append(i)
        for i in range(len(subgrid)):
            if subgrid[i] == 0:
                subgrid[i] = output_grid.pop()
    return subgrids 

def subgrids_to_sudoku(subgrids):
    sudoku = [[0,0,0,0,0,0,0,0,0]]*9
    sudoku = np.array(sudoku)
    sudoku = np.reshape(sudoku,(9,9))
    for list_id in range(len(subgrids)):
        start_row = (list_id//3)*3
        start_col = (list_id%3)*3
        subgrid = subgrids[list_id]
        subgrid.reverse()
        for i in range(3):
            for j in range(3):
                sudoku[start_row+i][start_col+j] = subgrid.pop()
    
    return sudoku

class Sudoku():
    def __init__(self):
        # self.puzzle = '920870060080020390007903010340059780700104002019280604004065809035090100006402070'
        # self.original_problem = generate_puzzle(self.puzzle)

        self.puzzle = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
        self.target = generate_puzzle('864371259325849761971265843436192587198657432257483916689734125713528694542916378')

        self.empty_sudoku = generate_puzzle(self.puzzle)
        self.subgrids = return_initialized_puzzle(self.empty_sudoku)
        self.sudoku = subgrids_to_sudoku(self.subgrids)

        self.binary_map = generate_puzzle(self.get_binary_map())
        
        self.last_action = [0]*9

    def get_binary_map(self):
        binary_map = ''
        for i in self.puzzle:
            if (i == '0'):
                binary_map += '0'
            else:
                binary_map += '1'
        return binary_map

    def reset(self):
        self.last_action = [0]*9
        self.empty_sudoku = generate_puzzle(self.puzzle)
        self.subgrids = return_initialized_puzzle(self.empty_sudoku)
        self.sudoku = subgrids_to_sudoku(self.subgrids)

    def get_subgrid_state(self,genome_id):
        subgrids = get_subgrids(self.sudoku)
        return subgrids[genome_id]


    def step(self,current_action,genome_id):

        last_action = self.last_action[genome_id]

        subgrids = get_subgrids(self.sudoku)
        subgrid = subgrids[genome_id]
        
        row = (genome_id//3)*3
        col = (genome_id%3)*3
        abs_r_0 = row + last_action//3
        abs_c_0 = col + last_action%3

        abs_r_1 = row + current_action//3
        abs_c_1 = col + current_action%3

        if self.binary_map[abs_r_0][abs_c_0] != 1 and self.binary_map[abs_r_1][abs_c_1] != 1:
            temp = subgrid[last_action]
            subgrid[last_action] = subgrid[current_action]
            subgrid[current_action] = temp

            subgrids[genome_id] = subgrid
            self.sudoku = subgrids_to_sudoku(subgrids)
        
        self.last_action[genome_id] = current_action
        
    def render(self):
        # clearscreen = lambda: os.system('clear')
        # clearscreen()
        print(self.sudoku)