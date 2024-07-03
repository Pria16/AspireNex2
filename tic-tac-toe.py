import math

# Initialize the board
def create_board():
    return [' ' for _ in range(9)]

# Print the board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check if the current board is a win for the given player
def is_winner(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]
    return [player, player, player] in win_conditions

# Check if the board is full (draw)
def is_draw(board):
    return ' ' not in board

# Get the available moves
def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    if is_winner(board, 'O'):
        return 1
    elif is_winner(board, 'X'):
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Get the best move for the AI
def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, -math.inf, math.inf, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Main game loop
def play_game():
    board = create_board()
    human_player = 'X'
    ai_player = 'O'
    current_player = human_player

    while True:
        print_board(board)
        if current_player == human_player:
            move = int(input('Enter your move (0-8): '))
            if board[move] == ' ':
                board[move] = human_player
                if is_winner(board, human_player):
                    print_board(board)
                    print('Human wins!')
                    break
                current_player = ai_player
        else:
            print("AI is thinking...")
            move = get_best_move(board)
            board[move] = ai_player
            print("AI has made its move:")
            print_board(board)
            if is_winner(board, ai_player):
                print('AI wins!')
                break
            current_player = human_player

        if is_draw(board):
            print_board(board)
            print('It\'s a draw!')
            break
        print("\nNext move:\n")

play_game()
