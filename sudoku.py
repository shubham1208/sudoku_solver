board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def valid(board, num, pos):
    
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        

def disp_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i !=0:
            print("--------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end = "")

            if j == 8:
                print(board[i][j])

            else:
                print(str(board[i][j]) + " ", end = "")

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return(i, j) #y, x


disp_board(board)