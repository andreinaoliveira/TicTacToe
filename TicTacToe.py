

def NewGame():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return board


def PrintBoard(board):
    print("""
        Tic Tac Toe
Player 1 (X) - Player 2 (O)
        |      |      
     {}  |   {}  |   {}  
  ______|______|______
        |      |      
     {}  |   {}  |   {}  
  ______|______|______
        |      |      
     {}  |   {}  |   {}  
        |      |
    """.format(board[0][0],
               board[0][1],
               board[0][2],
               board[1][0],
               board[1][1],
               board[1][2],
               board[2][0],
               board[2][1],
               board[2][2]))


def Play(board, player):
    number = int(input('Player {}, enter a number: '.format(player)))
    if player == 1:
        choice = 'X'
    else:
        choice = 'O'
    if number == 1:
        board[0][0] = choice
    elif number == 2:
        board[0][1] = choice
    elif number == 3:
        board[0][2] = choice
    elif number == 4:
        board[1][0] = choice
    elif number == 5:
        board[1][1] = choice
    elif number == 6:
        board[1][2] = choice
    elif number == 7:
        board[2][0] = choice
    elif number == 8:
        board[2][1] = choice
    else:
        board[2][2] = choice


def Win(board):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 1
        else:
            return 2
    if board[0][2] == board[1][1] and board[1][1] == board [2][0]:
        if board[0][0] == 'X':
            return 1
        else:
            return 2

    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        if board[0][0] == 'X':
            return 1
        else:
            return 2
    if board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        if board[0][0] == 'X':
            return 1
        else:
            return 2
    if board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        if board[0][0] == 'X':
            return 1
        else:
            return 2

    if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        if board[0][0] == 'X':
            return 1
        else:
            return 2
    if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        if board[0][0] == 'X':
            return 1
        else:
            return 2
    if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        if board[0][0] == 'X':
            return 1
        else:
            return 2
    return 0
