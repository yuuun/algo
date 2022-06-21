from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def solution(board):
    N = len(board)
    costs = [[float('inf')] * N for _ in range(N)]

    deq = deque()
    deq.append((0, 0, 0, 1))
    deq.append((0, 0, 0, 3))
    costs[0][0] = 0
    while deq:
        x, y, cost, dir = deq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            tmp_cost = cost + 100 if dir == k else cost + 600
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0 and tmp_cost <= costs[nx][ny]:
                    costs[nx][ny] = tmp_cost
                    deq.append((nx, ny, tmp_cost, k))

    return costs[-1][-1]
print(solution([[0,0,0],[0,0,0],[0,0,0]]), 900)
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]), 3800)
print(solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]), 3000)
print(solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]), 4500)