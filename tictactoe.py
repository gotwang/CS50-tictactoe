"""
Tic Tac Toe Player
"""

import math
import copy

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
    empties = 0
    for row in board :
        for cell in row :
            if cell == None :
                empties += 1
    if empties % 2 == 1 :
        return X
    else :
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == None :
                cell = (row, col)
                possible.add(cell)
    return possible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board) :
        raise ValueError
    copyBoard = copy.deepcopy(board)
    copyBoard[action[0]][action[1]] = player(board)
    return copyBoard


def checkWinner(three):
    if len(three) == 1 and EMPTY not in three:
        return True
    else :
        return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    one = [board[0][0], board[0][1], board[0][2]]
    topRow = set(one)
    if checkWinner(topRow):
        return board[0][0]
    two = [board[1][0], board[1][1], board[1][2]]
    secondRow = set(two)
    if checkWinner(secondRow):
        return board[1][0]
    three = [board[2][0], board[2][1], board[2][2]]
    thirdRow = set(three)
    if checkWinner(thirdRow):
        return board[2][0]
    four = [board[0][0], board[1][0], board[2][0]]
    firstCol = set(four)
    if checkWinner(firstCol):
        return board[0][0]
    five = [board[0][1], board[1][1], board[2][1]]
    secondCol = set(five)
    if checkWinner(secondCol):
        return board[0][1]
    six = [board[0][2], board[1][2], board[2][2]]
    thirdCol = set(six)
    if checkWinner(thirdCol):
        return board[0][2]
    seven = [board[0][0], board[1][1], board[2][2]]
    diag = set(seven)
    if checkWinner(diag):
        return board[0][0]
    eight = [board[2][0], board[1][1], board[0][2]]
    diag2 = set(eight)
    if checkWinner(diag2):
        return board[2][0]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empties = False
    for row in board :
        for cell in row :
            if cell == None :
                empties = True
                continue
    result = winner(board)
    if result != None or not empties:
        return True
    else :
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result == X:
        return 1
    if result == O:
        return -1
    else :
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        v = maxValue(board)
    else :
        v = minValue(board)
    for action in actions(board):
        newBoard = result(board, action)
        if player(board) == X:
            if minValue(newBoard) == v:
                return action
        else :
            if maxValue(newBoard) == v:
                return action

def maxValue(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        newBoard = result(board, action)
        v = max(v, minValue(newBoard))
    return v

def minValue(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        newBoard = result(board, action)
        v = min(v, maxValue(newBoard))
    return v
        

