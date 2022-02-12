# skill[0] = [type, r1, c1, r2, c2, degree]
# 시간 초과
def solution1(board, skill):
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    board[r][c] -= degree
        else:
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    board[r][c] += degree      
    answer = 0   
    for bo in board:
        for b in bo:
            if b > 0:
                answer += 1
    return answer

# skill[0] = [type, r1, c1, r2, c2, degree]
# 누적 합
def solution(board, skill):
    tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for t, r1, c1, r2, c2, degree in skill:
        r2 += 1
        c2 += 1
        if t == 1:
            tmp[r1][c1] -= degree
            tmp[r2][c2] -= degree
            tmp[r1][c2] += degree
            tmp[r2][c1] += degree
        else:
            tmp[r1][c1] += degree
            tmp[r2][c2] += degree
            tmp[r1][c2] -= degree
            tmp[r2][c1] -= degree
            
    for r in range(1, len(tmp)):
        for c in range(len(tmp[0])):
            tmp[r][c] += tmp[r - 1][c]
    for c in range(1, len(tmp[0])):
        for r in range(len(tmp)):
            tmp[r][c] += tmp[r][c - 1]
    
    answer = 0
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] += tmp[r][c]
            
    for bo in board:
        for b in bo:
            if b > 0:
                answer += 1
    return answer