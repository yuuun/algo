# TBD
from collections import deque
n, m, k = map(int, input().split()) # n: 격자, m: 상어, k: 냄새 사라지는 횟수

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 위, 아래, 왼, 오른
smell = [[[] for _ in range(n)] for _ in range(n)]
shark = {}
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] != 0:
            s = tmp[j] - 1
            smell[i][j] = [k, s, False]
            # shark.append((tmp[j], i, j))
            shark[s] = [i, j]

for i, t in enumerate(map(int, input().split())):
    shark[i].append(t - 1)

dire = []
for _ in range(m):
    tmp = []
    for _ in range(4):
        tmp.append(list(map(lambda x: int(x) - 1, input().split())))
    dire.append(tmp)

visited = [False] * m
def reduce_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j]:
                if smell[i][j][0] > 1:
                    smell[i][j][0] -= 1
                    smell[i][j][2] = False
                else:
                    smell[i][j] = []

def check_direction(x, y, s, d):
    tmp = []
    for nd in dire[s][d]:
        nx, ny = x + dxy[nd][0], y + dxy[nd][1]
        if 0 <= nx < n and 0 <= ny < n:
            if smell[nx][ny] == []:
                shark[s] = [nx, ny, nd]
                smell[nx][ny] = [k + 1, s, False]
                return False
            elif smell[nx][ny][1] == s and tmp == []:
                tmp = [nx, ny, nd]
            elif smell[nx][ny][0] == k + 1 and not smell[nx][ny][2]: # 현 시점에서 이미 선점한 상어가 있을 경우는 제외시켜줄 것
                # del shark[smell[nx][ny][1]]
                remove_shark = smell[nx][ny][1]
                shark[s] = [nx, ny, nd]
                smell[nx][ny] = [k + 1, s, True]
                return [remove_shark]
    
    return tmp

def move_shark():
    for s, val in sorted(shark.items(), reverse=True):
        x, y, d = val
        tmp = check_direction(x, y, s, d)
        if tmp:
            if len(tmp) == 1:
                del shark[tmp[0]]
            else:
                nx, ny, nd = tmp
                smell[nx][ny] = [k + 1, s, True]
                shark[s] = [nx, ny, nd]

    
ans = 1
while ans < 1000:
    move_shark()
    reduce_smell()
    if len(shark) == 1:
        break
    ans += 1
print(ans if ans < 1000 else -1)