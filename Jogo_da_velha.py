import random

# Inicializa o tabuleiro
board = [' ' for _ in range(9)]

# Define a função para imprimir o tabuleiro
def print_board():
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

# Função para verificar se há um vencedor
def check_winner():
    # Verifica linhas
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return board[i]
    # Verifica colunas
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]
    # Verifica diagonais
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]
    # Verifica empate
    if ' ' not in board:
        return 'tie'
    # Jogo ainda não terminou
    return None

# Função para obter a jogada do usuário
def get_user_move():
    while True:
        move = input("Sua jogada (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move)-1] == ' ':
            return int(move) - 1
        print("Jogada inválida. Tente novamente.")

# Função para fazer a jogada do computador
def make_computer_move():
    # Verifica se há uma jogada vencedora
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_winner() == 'X':
                return
            board[i] = ' '
    # Verifica se há uma jogada que bloqueia o usuário
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_winner() == 'O':
                board[i] = 'X'
                return
            board[i] = ' '
    # Faz uma jogada aleatória
    empty_spots = [i for i in range(9) if board[i] == ' ']
    board[random.choice(empty_spots)] = 'X'

# Inicia o jogo
print_board()
print("Computador joga primeiro.")
while True:
    make_computer_move()
    print_board()
    winner = check_winner()
    if winner == 'X':
        print("Computador venceu!")
        break
    elif winner == 'O':
        print("Você venceu!")
        break
    elif winner == 'tie':
        print("Empate!")
        break
    user_move = get_user_move()
    board[user_move] = 'O'







