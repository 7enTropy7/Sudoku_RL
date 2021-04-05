import numpy as np
import math
import random

def generate_puzzle(string):
    list1=[]
    list1[:0]=string
    for i in range(0, len(list1)):
        list1[i] = int(list1[i])
    list1 = np.array(list1)
    list1 = np.reshape(list1,(9,9))
    return list1

class Sudoku():
    def __init__(self):
        self.puzzle = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
        self.sudoku = generate_puzzle(self.puzzle)
        self.target = generate_puzzle('864371259325849761971265843436192587198657432257483916689734125713528694542916378')
        self.pos = [0,0]
        self.binary_map = generate_puzzle(self.get_binary_map())
        self.reward = 0
        self.reward_dict = {
            1:-4,
            2:-3,
            3:-2,
            4:-1,
            5:0,
            6:1,
            7:2,
            8:3,
            9:4
        }


    def get_binary_map(self):
        binary_map = ''
        for i in self.puzzle:
            if (i == '0'):
                binary_map += '0'
            else:
                binary_map += '1'
        return binary_map

    def reset(self):
        self.pos = [0,0]

    def step(self,action):
        
        if action == 0:
            if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                self.sudoku[self.pos[0]][self.pos[1]] = 1
                
                # calculate reward
            else:
                # calculate punishment
                pass
        elif action == 1:
            if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                self.sudoku[self.pos[0]][self.pos[1]] = 2
                
                # calculate reward
            else:
                # calculate punishment
                pass
        elif action == 2:
            if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                self.sudoku[self.pos[0]][self.pos[1]] = 3
                
                # calculate reward
            else:
                # calculate punishment
                pass
        elif action == 3:
            if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                self.sudoku[self.pos[0]][self.pos[1]] = 4
                
                # calculate reward
            else:
                # calculate punishment
                pass
        elif action == 4:
            if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                self.sudoku[self.pos[0]][self.pos[1]] = 5
                
                # calculate reward
            else:
                # calculate punishment
                pass
        elif action == 5:
            if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                self.sudoku[self.pos[0]][self.pos[1]] = 6
                
                # calculate reward
            else:
                # calculate punishment
                pass
        elif action == 6:
            if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                self.sudoku[self.pos[0]][self.pos[1]] = 7
                
                # calculate reward
            else:
                # calculate punishment
                pass
        elif action == 7:
            if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                self.sudoku[self.pos[0]][self.pos[1]] = 8
                
                # calculate reward
            else:
                # calculate punishment
                pass
        elif action == 8:
            if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                self.sudoku[self.pos[0]][self.pos[1]] = 9

                # calculate reward
            else:
                # calculate punishment
                pass
        elif action == 9: # Up
            if self.pos[0] == 0:
                self.pos[0] = 8
            else:
                self.pos[0] -= 1

            if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                # calculate reward based on binary map
            else:
                # calculate punishment
                pass

        elif action == 10: # Down
            if self.pos[0] == 8:
                self.pos[0] = 0
            else:
                self.pos[0] += 1

            if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                # calculate reward based on binary map
            else:
                # calculate punishment
                pass
            
        elif action == 11: # Left
            if self.pos[1] == 0:
                self.pos[1] = 8
            else:
                self.pos[1] -= 1

            if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                # calculate reward based on binary map
            else:
                # calculate punishment
                pass
        
        elif action == 12: # Right
            if self.pos[1] == 8:
                self.pos[1] = 0
            else:
                self.pos[1] += 1

            if self.binary_map[self.pos[0]][self.pos[1]] == 0:
                # calculate reward based on binary map
            else:
                # calculate punishment
                pass

    
    def render(self):
        pass

