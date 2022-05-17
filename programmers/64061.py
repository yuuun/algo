from collections import deque
def solution(board, moves):
    maps = [deque() for _ in range(len(board))]
    for j in range(len(board[0])):
        for i in range(len(board)):
            if board[i][j] == 0:
                continue
            maps[j].append(board[i][j])
    tmp = deque()
    cnt = 0
    for b in moves:
        b -= 1
        if maps[b]:
            t = maps[b].popleft()
            if tmp and tmp[-1] == t:
                tmp.pop()
                cnt += 2
            else:
                tmp.append(t)
    return cnt

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]), 4)