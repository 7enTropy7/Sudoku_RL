import numpy as np

puzzle = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'

solved = '864371259325849761971265843436192587198657432257483916689734125713528694542916378'

def generate_puzzle(string):
    list1=[]
    list1[:0]=string
    for i in range(0, len(list1)):
        list1[i] = int(list1[i])
    list1 = np.array(list1)
    list1 = np.reshape(list1,(9,9))
    return list1

sudoku = generate_puzzle(puzzle)
target = generate_puzzle(solved)

# print(sudoku)
# print(sudoku[5][5])

def get_row_col_subgrid(x,y,sudoku):
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
        
    return row,col,subgrid

# print(get_row_col_subgrid(5,5,sudoku))

print(target)
# print('------------------------')
# print(sudoku)

if (sudoku == target).all():
    print('Oui')
else:
    print('No')

