import numpy as np

sudoku_puzzle =[[9,6,20,7,8,5,0,0],
[1,0,5,0,0,9,3,0,0],
[3,0,0,5,0,0,8,2,0],
[0,0,1,0,0,0,0,7,0],
[6,0,0,0,5,0,0,0,8],
[0,0,0,6,0,3,9,0,5],
[0,1,8,0,0,5,0,0,1],
[0,0,6,8,3,2,7,0,0],
[7,5,3,1,9,0,4,8,0],

]
def possibility(Row,Column,Num):
    global sudoku_puzzle
    for i in range(0,9):
        if sudoku_puzzle[Row][i]==Num:
            return False
        
        for i in range(0,9):
            if sudoku_puzzle[i][Column]==Num:
                return False
            
                
        x = (Column//3)*3
        y = (Row//3)*3
        for i in range(0,3):
            for j in range(0,3):
                if sudoku_puzzle[y+1][x+1]==Num:
                    return False
        
                
                return True
            def solution():
                global sudoku_puzzle
                for Row in range(0,9):
                    for Column in range(0,9):
                         if sudoku_puzzle[Row][Column] ==0:
                             
                    for Num in range(1,10):
                            
                            if possibility(Row,Column,Num):
                                sudoku_puzzle[Row][Column] = Num
                                solution()
                                sudoku_puzzle[Row][Column] = 0
                                return
              print(np.matrix(sudoku_puzzle))

    
