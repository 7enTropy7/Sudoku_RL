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

def get_row_col_subgrid(x,y,val,sudoku):
    col = []
    for row in sudoku:
        col.append(row[y])
    
    row = sudoku[x].tolist()

    subx = x//3
    suby = y//3

    subgrid = []
    startx, starty = subx*3,suby*3
    for i in range(3):
        for j in range(3):
            subgrid.append(sudoku[startx+i][starty+j])
        
    occ_row = row.count(val) - 1
    occ_col = col.count(val) - 1
    occ_subgrid = subgrid.count(val) - 1

    temp = 0
    duplicate_reset = False

    if occ_row == 0:
        temp += 1
    if occ_col == 0:
        temp += 1
    if occ_subgrid == 0:
        temp += 1
    if occ_row > 0 or occ_col > 0 or occ_subgrid > 0:
        duplicate_reset = True

    # if occ_row == 0:
    #     temp += 1
    # else:
    #     temp -= occ_row
    # if occ_col == 0:
    #     temp += 1
    # else:
    #     temp -= occ_col
    # if occ_subgrid == 0:
    #     temp += 1
    # else:
    #     temp -= occ_subgrid

    return temp, duplicate_reset


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
            self.reward = 10
            self.done = True
            
        else:
            if action == 0:
                if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                    if self.sudoku[self.pos[0]][self.pos[1]] != 1:
                        self.sudoku[self.pos[0]][self.pos[1]] = 1
                        # Checking for occurence in row,col,subgrid
                        temp,duplicate_reset = get_row_col_subgrid(self.pos[0],self.pos[1],1,self.sudoku)
                        # Positive Reward for single occurence
                        if not duplicate_reset:
                            self.reward = temp
                        else:
                            self.reward = -3
                            self.reset()
                    else:
                        self.reward = -0.3
                else:
                    self.reward = -1

            elif action == 1:
                if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                    if self.sudoku[self.pos[0]][self.pos[1]] != 2:
                        self.sudoku[self.pos[0]][self.pos[1]] = 2
                        # Checking for occurence in row,col,subgrid
                        temp, duplicate_reset = get_row_col_subgrid(self.pos[0],self.pos[1],2,self.sudoku)
                        # Positive Reward for single occurence
                        if not duplicate_reset:
                            self.reward = temp
                        else:
                            self.reward = -3
                            self.reset()
                    else:
                        self.reward = -0.3
                else:
                    self.reward = -1

            elif action == 2:
                if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                    if self.sudoku[self.pos[0]][self.pos[1]] != 3:
                        self.sudoku[self.pos[0]][self.pos[1]] = 3
                        # Checking for occurence in row,col,subgrid
                        temp,duplicate_reset = get_row_col_subgrid(self.pos[0],self.pos[1],3,self.sudoku)
                        # Positive Reward for single occurence
                        if not duplicate_reset:
                            self.reward = temp
                        else:
                            self.reward = -3
                            self.reset()
                    else:
                        self.reward = -0.3
                else:
                    self.reward = -1

            elif action == 3:
                if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                    if self.sudoku[self.pos[0]][self.pos[1]] != 4:
                        self.sudoku[self.pos[0]][self.pos[1]] = 4
                        # Checking for occurence in row,col,subgrid
                        temp,duplicate_reset = get_row_col_subgrid(self.pos[0],self.pos[1],4,self.sudoku)
                        # Positive Reward for single occurence
                        if not duplicate_reset:
                            self.reward = temp
                        else:
                            self.reward = -3
                            self.reset()
                    else:
                        self.reward = -0.3
                else:
                    self.reward = -1

            elif action == 4:
                if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                    if self.sudoku[self.pos[0]][self.pos[1]] != 5:
                        self.sudoku[self.pos[0]][self.pos[1]] = 5
                        # Checking for occurence in row,col,subgrid
                        temp,duplicate_reset = get_row_col_subgrid(self.pos[0],self.pos[1],5,self.sudoku)
                        # Positive Reward for single occurence
                        if not duplicate_reset:
                            self.reward = temp
                        else:
                            self.reward = -3
                            self.reset()
                    else:
                        self.reward = -0.3
                else:
                    self.reward = -1

            elif action == 5:
                if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                    if self.sudoku[self.pos[0]][self.pos[1]] != 6:
                        self.sudoku[self.pos[0]][self.pos[1]] = 6
                        # Checking for occurence in row,col,subgrid
                        temp,duplicate_reset = get_row_col_subgrid(self.pos[0],self.pos[1],6,self.sudoku)
                        # Positive Reward for single occurence
                        if not duplicate_reset:
                            self.reward = temp
                        else:
                            self.reward = -3
                            self.reset()
                    else:
                        self.reward = -0.3
                else:
                    self.reward = -1

            elif action == 6:
                if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                    if self.sudoku[self.pos[0]][self.pos[1]] != 7:
                        self.sudoku[self.pos[0]][self.pos[1]] = 7
                        # Checking for occurence in row,col,subgrid
                        temp,duplicate_reset = get_row_col_subgrid(self.pos[0],self.pos[1],7,self.sudoku)
                        # Positive Reward for single occurence
                        if not duplicate_reset:
                            self.reward = temp
                        else:
                            self.reward = -3
                            self.reset()
                    else:
                        self.reward = -0.3
                else:
                    self.reward = -1

            elif action == 7:
                if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                    if self.sudoku[self.pos[0]][self.pos[1]] != 8:
                        self.sudoku[self.pos[0]][self.pos[1]] = 8
                        # Checking for occurence in row,col,subgrid
                        temp,duplicate_reset = get_row_col_subgrid(self.pos[0],self.pos[1],8,self.sudoku)
                        # Positive Reward for single occurence
                        if not duplicate_reset:
                            self.reward = temp
                        else:
                            self.reward = -3
                            self.reset()
                    else:
                        self.reward = -0.3
                else:
                    self.reward = -1

            elif action == 8:
                if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                    if self.sudoku[self.pos[0]][self.pos[1]] != 9:
                        self.sudoku[self.pos[0]][self.pos[1]] = 9
                        # Checking for occurence in row,col,subgrid
                        temp,duplicate_reset = get_row_col_subgrid(self.pos[0],self.pos[1],9,self.sudoku)
                        # Positive Reward for single occurence
                        if not duplicate_reset:
                            self.reward = temp
                        else:
                            self.reward = -3
                            self.reset()
                    else:
                        self.reward = -0.3
                else:
                    self.reward = -1
                    
            elif action == 9: # Up
                if self.pos[0] == 0:
                    self.pos[0] = 8
                else:
                    self.pos[0] -= 1

                if self.binary_map[self.pos[0]][self.pos[1]] == 1:
                    # calculate reward based on binary map
                    # if self.sudoku[self.pos[0]][self.pos[1]] == 0:
                    #     self.reward = 0.2
                    
                    # calculate punishment
                    self.reward = -1
                    
            elif action == 10: # Down
                if self.pos[0] == 8:
                    self.pos[0] = 0
                else:
                    self.pos[0] += 1

                if self.binary_map[self.pos[0]][self.pos[1]] == 1:
                    # calculate reward based on binary map
                    # if self.sudoku[self.pos[0]][self.pos[1]] == 0:
                    #     self.reward = 0.2
                    
                    # calculate punishment
                    self.reward = -1
                
            elif action == 11: # Left
                if self.pos[1] == 0:
                    self.pos[1] = 8
                else:
                    self.pos[1] -= 1

                if self.binary_map[self.pos[0]][self.pos[1]] == 1:
                    # calculate reward based on binary map
                    # if self.sudoku[self.pos[0]][self.pos[1]] == 0:
                    #     self.reward = 0.2
                    
                    # calculate punishment
                    self.reward = -1
            
            elif action == 12: # Right
                if self.pos[1] == 8:
                    self.pos[1] = 0
                else:
                    self.pos[1] += 1

                if self.binary_map[self.pos[0]][self.pos[1]] == 1:
                    # calculate reward based on binary map
                    # if self.sudoku[self.pos[0]][self.pos[1]] == 0:
                    #     self.reward = 0.2
                    
                    # calculate punishment
                    self.reward = -1
            
            num_0 = 0
            for r in self.sudoku:
                num_0 += r.tolist().count(0)

            print('Percentage Filled : ',100*(81-num_0)/81)

        return self.pos,self.reward,self.done    

    def render(self):
        clearscreen = lambda: os.system('clear')
        clearscreen()
        print(self.sudoku)

