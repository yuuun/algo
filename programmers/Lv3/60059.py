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
			# lock에 해당하는 부분이 0이어도, 2이어도 문제 조건에 충족하지 않기 때문에 1인지 여부를 확인
            if tmp_board[n + i - 1][n + j - 1] != 1:
                return False
    return True
            
def solution(key, lock):
    n = len(key) # key의 길이
    m = len(lock) # lock의 길이
    board = [[0] * (2 * n + m - 2) for _ in range(2 * n + m - 2)]
    
    # 자물쇠를 board의 중앙에 배치
    for i in range(m):
        for j in range(m):
            board[n + i - 1][n + j - 1] = lock[i][j]
    
    for _ in range(4):
        key = rotate(key)   # 4번 회전시켜가면서 key와 lock를 매칭시키기
        for i in range(n + m - 1):
            for j in range(n + m - 1):
                isFilled = check_board(board, key, i, j, m, n)
                if isFilled:
                    return True
    return False