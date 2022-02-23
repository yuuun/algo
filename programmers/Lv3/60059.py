from copy import deepcopy
def rotate(arr):
    return [list(elem) for elem in zip(*arr[::-1])]

def check_board(board, key, x, y, m, n):
    tmp_board = deepcopy(board)
    for i in range(len(key)):
        for j in range(len(key)):
            tmp_board[x + i][y + j] += key[i][j]
    
    for i in range(m):
        for j in range(m):
            if tmp_board[n + i - 1][n + j - 1] != 1:
                return False, board
    return True, tmp_board
            
def solution(key, lock):
    n = len(key) # key의 길이
    m = len(lock) # lock의 길이
    board = [[0] * (2 * n + m - 2) for _ in range(2 * n + m - 2)]
    
    # 자물쇠를 board의 중앙에 배치
    for i in range(m):
        for j in range(m):
            board[n + i - 1][n + j - 1] = lock[i][j]
    
    for _ in range(4):
        key = rotate(key)
        for i in range(n + m - 1):
            for j in range(n + m - 1):
                isFilled, board = check_board(board, key, i, j, m, n)
                if isFilled:
                    return True
    return False