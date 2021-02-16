"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None
CURRENT = 0
PLAYERS = {0: X, 1:O}

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return None
    else:
        return PLAYERS[CURRENT]


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    else:
        moves = set()
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    moves.add((i,j))
        return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    turn = player(board)
    global CURRENT
    CURRENT = (CURRENT+1)%2
    if action[0] < 0 or action[0] > 2 or action[1] < 0 or action[1] > 2:
        raise Exception("Invalid Action")
    else:
        board[action[0]][action[1]] = turn

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != EMPTY:
        return board[1][1]
    
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
    
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)
    if game_winner is None:
        return 0
    
    if game_winner == X:
        return 1
    else:
        return -1


def minimax_helper(board, p, alpha, beta):
    if terminal(board):
        return [None, utility(board)]

    possible_moves = actions(board)
    optimal = None
    if p == X:
        max_val = -2
        for move in possible_moves:
            board[move[0]][move[1]] = p
            res = minimax_helper(board, O, alpha, beta)
            board[move[0]][move[1]] = EMPTY
            if res[1] > max_val:
                max_val = res[1]
                optimal = move
            alpha = max(alpha, max_val)
            if alpha >= beta:
                break
        return [optimal, max_val]
    else:
        min_val = 2
        for move in possible_moves:
            board[move[0]][move[1]] = p
            res = minimax_helper(board, X, alpha, beta)
            board[move[0]][move[1]] = EMPTY
            if res[1] < min_val:
                min_val = res[1]
                optimal = move
            beta = min(beta, min_val)
            if beta <= alpha:
                break
        return [optimal, min_val]
        