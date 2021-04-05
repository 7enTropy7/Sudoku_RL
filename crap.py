import numpy as np

puzzle = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'


def generate_puzzle(string):
    list1=[]
    list1[:0]=string
    for i in range(0, len(list1)):
        list1[i] = int(list1[i])
    list1 = np.array(list1)
    list1 = np.reshape(list1,(9,9))
    return list1

sudoku = generate_puzzle(puzzle)

print(sudoku)
#print(sudoku[2][1])

def get_row_col_subgrid(x,y,sudoku):
    col = []
    for row in sudoku:
        col.append(row[y])
    
    
    return sudoku[x].tolist(),col


# print(sudoku[4-1][1]) # Up
# print(sudoku[4+1][1]) # Down
# print(sudoku[4][1-1]) # Left
# print(sudoku[4][1+1]) # Right

# solved = '864371259325849761971265843436192587198657432257483916689734125713528694542916378'