import TicTacToe

board = TicTacToe.NewGame() #Inicialização da Matriz 3x3
player = 1 #Jogador que irá começar o jogo
win = 0 #Armazena o ganhador
rounds = 0 #Conta o número de rodadas

while True:
    if player == 3: #Define limite de dois jogadores, logo se passar de 2, volta para 1.
        player = 1

    TicTacToe.PrintBoard(board) #Função para imprimir o tabuleiro
    TicTacToe.Play(board, player) #Função para fazer a jogada, recebe o tabuleiro e o jogador

    win = TicTacToe.Win(board) #Checa se houve ganhadores.
    if win > 0:
        TicTacToe.PrintBoard(board)
        if win > 1:
            print("Player 2 Ganhou!")
        else:
            print("Player 1 Ganhou!")
        break

    player += 1 #Passa a vez para o próximo jogador
    rounds +=1 #Próximo round

    if rounds == 9: #Checa o empate
        TicTacToe.PrintBoard(board)
        print("EMPATE!")
        break
