import random

board = ['_', '_', '_',
         '_', '_', '_',
         '_', '_', '_']

winner = None
current_player = 'X'
game_is_on = True

def printboard(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print('----------')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print('----------')
    print(f'{board[6]} | {board[7]} | {board[8]}')

def get_user_input(board):
    user_input = int(input('Enter a number 1-9: '))
    if user_input >= 1 and user_input <= 9 and board[user_input - 1] == '_':
        board[user_input - 1] = current_player
    else:
        print('Oops! player is already on that spot')

def check_horizontal(board):
    if board[0] == board[1] == board[2] and board[0] != '_':
        winner = board[1]
        return True
    elif board[3] == board[4] == board[5] and board[3] != '_':
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[6] != '_':
        winner = board[7]
        return True

def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != '_':
        winner = board[3]
        return True
    elif board[1] == board[4] == board[7] and board[1] != '_':
        winner = board[4]
        return True
    elif board[2] == board[5] == board[8] and board[2] != '_':
        winner = board[5]
        return True

def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != '_':
        winner = board[4]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '_':
        winner = board[4]
        return True

def check_tie(board):
    if "_" not in board:
        printboard(board)
        print('It is a tie!')
        game_is_on = False

def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

def computer(board):
    while current_player == 'O':
        position = random.randint(0, 8)
        if board[position] == '_':
            board[position] = 'O'
            switch_player()

def check_win():
    if check_horizontal(board) or check_row(board) or check_diagonal(board):
        print(f'The winner is {winner}')

while game_is_on:
    printboard(board)
    get_user_input(board)
    check_win()
    check_tie(board)
    switch_player()
    computer(board)
    check_win()
    check_tie(board)
