import math

board = [' ' for _ in range(9)]  # initial board state

# Function to print Tic-Tac-Toe
def print_board(board):
    row = ""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print(row)
            row = ""
        row += " " + board[i]

    print(row)

# Function to determine if the game is over
def is_game_over(board):
    # Check horizontal lines
    for i in range(3):
        if board[i*3] == board[i*3+1] == board[i*3+2] != ' ':
            return True
    # Check vertical lines
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return True

    return False

# Minimax function
def minimax(board, depth, is_maximizing):
    if is_game_over(board):
        if is_maximizing:
            return {'score': -1}
        else:
            return {'score': 1}

    if ' ' not in board:
        return {'score': 0}

    if is_maximizing:
        best_score = -math.inf
        move = None
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)['score']
                board[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i

        return {
            'score': best_score,
            'move': move
        }

    else:
        best_score = math.inf
        move = None
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)['score']
                board[i] = ' '
                if score < best_score:
                    best_score = score
                    move = i

        return {
            'score': best_score,
            'move': move
        }
# Game loop
while True:
    print_board(board)
    if is_game_over(board):
        print("Game Over.")
        break
    if ' ' not in board:
        print("It's a draw.")
        break
    move = int(input("Your move (0-8): "))
    board[move] = 'X'
    if is_game_over(board):
        print_board(board)
        print("Game Over.")
        break
    print("AI is thinking...")
    move = minimax(board, 0, True)['move']
    board[move] = 'O'
