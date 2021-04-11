import numpy as np

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

def generate_puzzle(string):
    list1=[]
    list1[:0]=string
    for i in range(0, len(list1)):
        list1[i] = int(list1[i])
    list1 = np.array(list1)
    list1 = np.reshape(list1,(9,9))
    return list1

# puzzle = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
# sudoku = generate_puzzle(puzzle)
# print(sudoku)
# print(get_subgrids(sudoku)) 
# 

l = [0,0,1,2,3,3,3,4,4]
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


print(num_duplicates(l))