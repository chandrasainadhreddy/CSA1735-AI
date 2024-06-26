import math

# Constants representing players
PLAYER = 'X'
OPPONENT = 'O'

# Function to check for empty spots on the board
def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

# Function to evaluate the board and return a score based on who is winning
def evaluate(board):
    # Check rows for victory
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == PLAYER:
                return 10
            elif row[0] == OPPONENT:
                return -10

    # Check columns for victory
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == PLAYER:
                return 10
            elif board[0][col] == OPPONENT:
                return -10

    # Check diagonals for victory
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == PLAYER:
            return 10
        elif board[0][0] == OPPONENT:
            return -10

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == PLAYER:
            return 10
        elif board[0][2] == OPPONENT:
            return -10

    # No winner
    return 0

# Minimax function
def minimax(board, depth, is_max):
    score = evaluate(board)

    # If player wins
    if score == 10:
        return score - depth

    # If opponent wins
    if score == -10:
        return score + depth

    # If no moves left
    if not is_moves_left(board):
        return 0

    # If this is the maximizer's move
    if is_max:
        best = -math.inf

        # Traverse all cells
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER
                    best = max(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf

        # Traverse all cells
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = OPPONENT
                    best = min(best, minimax(board, depth + 1, not is_max))
                    board[i][j] = ' '
        return best

# Function to find the best move for the player
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    # Traverse all cells
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = PLAYER
                move_val = minimax(board, 0, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Example usage
if __name__ == "__main__":
    board = [
        ['X', 'O', 'X'],
        [' ', 'O', ' '],
        [' ', ' ', ' ']
    ]

    best_move = find_best_move(board)
    print(f"The best move is at position: {best_move}")
