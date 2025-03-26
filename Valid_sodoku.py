from collections import defaultdict
board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]



# Understood how to write a matrix for accessingg columns and rows, 
# using for loops to access rows, columns. Accessing rows is simple in 
# python just use for rows in matrix:
# for column we have to use two for loops

valid_set = {"1","2","3","4","5","6","7","8","9"}
hash_map = defaultdict(int)
hash_map_col = defaultdict(int)
hash_map_squares = defaultdict(int)

def Valid_Sudoku(board): 

    for row in board:
        hash_map.clear()
        print(row)
        for elements in row:    
                if elements != ".":
                    print(elements + "checking element")
                    if elements not in valid_set:
                        print("Not a valid sudoku")
                        return False
                    elif elements in hash_map.keys():
                        print("Not a valid sudoku")
                        return False
                    else:
                        hash_map[elements]+=1
    print("all rows adhere to rules")
                    
    for col in range(len(board)):
        hash_map_col.clear()
        print(row)
        for row in range(len(board)):    
                if board[row][col] != ".":
                    print(board[row][col] + "checking element")
                    if board[row][col] not in valid_set:
                        print("Not a valid sudoku")
                        return False
                    elif board[row][col] in hash_map_col.keys():
                        print("Not a valid sudoku")
                        return False
                    else:
                        hash_map_col[board[row][col]]+=1
    print("all columns adhere to rules")

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            hash_map_squares.clear()
            for row in range(box_row, box_row + 3):
                for col in range(box_col, box_col + 3):
                    num = board[row][col]
                    if num == ".":
                        continue
                    if num not in valid_set or num in hash_map_squares.keys():
                        print(f"Invalid sub-box at ({box_row}, {box_col}) (duplicate or invalid number: {num})")
                        return False
                    else:
                        hash_map_squares[board[row][col]]+=1
    print("All sub-boxes are valid.")
    return True
                    


if Valid_Sudoku(board):
     print("Yey!")
else:
     print("nay :(")


# Better short approach using the logic r //3 c//3
# below we are dynamically creatig sets for each row, column and square 
# and we iterate all elements row wise and with logic check the duplicates 
# in corresponding row or columns or squares and hence we do not need to 
# clear the set unlike the logic used above

row_set = defaultdict(set)
col_set = defaultdict(set)
squares_set = defaultdict(set)

def smart_validSudoku(board):

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] != ".":
                if board[row][col] not in valid_set:
                    return False
                elif(board[row][col] in row_set[row] or 
                     board[row][col] in col_set[col] or 
                     board[row][col] in squares_set[(row //3 ),(col // 3)]):
                    return False
                row_set[row].add(board[row][col])
                col_set[col].add(board[row][col])
                squares_set[(row // 3),(col // 3)].add(board[row][col])
    return True

if smart_validSudoku(board):
     print("Yey!")
else:
     print("nay :(")






