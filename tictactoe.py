"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = sum(row.count(X) for row in board)
    count_O = sum(row.count(O) for row in board)

    return X if count_X == count_O else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    new_board = [row[:] for row in board]
    if new_board[i][j] != EMPTY:
        raise Exception("Invalid move")
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O

    # Check columns
    for i in range(3):
        col = [board[j][i] for j in range(3)]
        if col.count(X) == 3:
            return X
        elif col.count(O) == 3:
            return O

    # Check diagonals
    if (board[0][0] == board[1][1] == board[2][2] == X) or (board[0][2] == board[1][1] == board[2][0] == X):
        return X
    elif (board[0][0] == board[1][1] == board[2][2] == O) or (board[0][2] == board[1][1] == board[2][0] == O):
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(all(cell is not EMPTY for cell in row) for row in board)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result_winner = winner(board)
    if result_winner == X:
        return 1
    elif result_winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    if current_player == X:
        best_val = -math.inf
        best_move = None
        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_val:
                best_val = value
                best_move = action
        return best_move
    else:
        best_val = math.inf
        best_move = None
        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_val:
                best_val = value
                best_move = action
        return best_move


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
