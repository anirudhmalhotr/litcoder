def checkSudoku(board):
    """
    Checks the validity of a Sudoku Board
    - Takes the board as an array as input
    """
    
    def isValid(arr):
        """
        Checks if array has valid sudoku values
        """
        arr = [i for i in arr if i!='.']
        return len(set(arr)) == len(arr)
    
    #check rows and columns
    for i in range(9):
        if not isValid(board[i]) or not isValid([board[j][i] for j in range(9)]):
            return "NO"
    
    #Check sub box
    for i in range(0,9,3):
        for j in range (0,9,3):
            subgrid = [board[x][y] for x in range (i,i+3) for y in range(j,j+3)]
            if not isValid(subgrid):
                return "NO"
    
    return "YES"
    
#Main
board = []
n = int(input())
for _ in range(n):
    row = input().strip().split()
    board.append(row)
    
result = checkSudoku(board)
print(result)