import TicTacToe

board = TicTacToe.NewGame()
player = 1
win = 0
rounds = 0

while True:
    if player == 3:
        player = 1
    TicTacToe.PrintBoard(board)
    TicTacToe.Play(board, player)
    win = TicTacToe.Win(board)
    if win > 0:
        TicTacToe.PrintBoard(board)
        if win > 1:
            print("Player 2 Ganhou!")
        else:
            print("Player 1 Ganhou!")
        break
    player += 1
    rounds +=1
    if rounds == 9:
        TicTacToe.PrintBoard(board)
        print("EMPATE!")
        break
