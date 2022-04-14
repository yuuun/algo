from collections import deque
def solution(m, n, board):
    for x in range(m):
        board[x] = list(board[x])
    answer = 0
    def step_one():
        earse = deque()
        for x in range(m - 1):
            for y in range(n - 1):
                if board[x][y] == 0:
                    continue
                t = board[x][y]
                cnt = 1
                for dx, dy in [[0, 1], [1, 0], [1, 1]]:
                    nx, ny = x + dx, y + dy
                    if board[nx][ny] == t:
                        cnt += 1
                    else:
                        break
                if cnt == 4:
                    earse.append([x, y])
        if not earse:
            return 0
        
        while earse:
            x, y = earse.popleft()
            board[x][y] = 0
            for dx, dy in [[0, 1], [1, 0], [1, 1]]:
                nx, ny = x + dx, y + dy
                board[nx][ny] = 0
        
        tmp_cnt = 0
        for j in range(n):
            q = deque()
            for i in range(m - 1, -1, -1):
                if board[i][j] != 0:
                    q.append(board[i][j])
                else:
                    tmp_cnt += 1
            t = m - 1
            while q:
                board[t][j] = q.popleft()
                t -= 1
            for i in range(t, -1, -1):
                board[i][j] = 0
        
        return tmp_cnt

    while True:
        tmp_cnt = step_one()
        if tmp_cnt == 0:
            break

    for x in range(m):
        for y in range(n):
            if board[x][y] == 0:
                answer += 1

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]), 14)
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]), 15)
print(solution(4, 4, ["ABCD", "BACE", "BCDD", "BCDD"]), 8)