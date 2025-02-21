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

#    return [['X', EMPTY, EMPTY],
#            [EMPTY, 'X', EMPTY],
#            [EMPTY, EMPTY, EMPTY]]


def player(board):

    x_count = 0
    o_count = 0
    
    for row in board:
        x_count += row.count('X')
        o_count += row.count('O')

    if x_count <= o_count:
        return 'X'
    else:
        return 'O'


def actions(board):
    actions_list = [] #lista para que se puedan ordenar en vez de un set
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                actions_list.append((i, j))  # Agrega la acción en orden
    return actions_list


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    # Verificar filas
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not None:
            return row[0]
    
    # Verificar columnas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    
    # Verificar diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    
    # Si no hay ganador
    return None


def terminal(board):
    # Si hay un ganador, el juego ha terminado
    if winner(board) is not None:
        return True
    
    # Si el tablero está lleno (sin espacios vacíos), el juego terminó (empate)
    for row in board:
        if None in row:  # Si hay alguna casilla vacía
            return False  # El juego sigue en curso
    
    # Si el tablero está lleno y no hay ganador, es un empate
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
