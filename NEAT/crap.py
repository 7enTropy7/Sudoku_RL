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

puzzle = '920870060080020390007903010340059780700104002019280604004065809035090100006402070'
        
sudoku = generate_puzzle(puzzle)
print(sudoku)
# print(get_subgrids(sudoku)) 


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
# print(num_duplicates(l))


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


subgrids = return_initialized_puzzle(sudoku)
print(subgrids)
sudoku = subgrids_to_sudoku(subgrids)
print(sudoku)