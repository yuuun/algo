import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())  # n: 격자, m: 상어, k: 냄새 사라지는 횟수

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # 위, 아래, 왼, 오른
smell = [[[] for _ in range(n)] for _ in range(n)]
shark = {}
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] != 0:
            s = tmp[j] - 1
            smell[i][j] = [k, s]
            shark[s] = [i, j]

for i, t in enumerate(map(int, input().split())):
    shark[i].append(t - 1)

dire = []
for _ in range(m):
    tmp = []
    for _ in range(4):
        tmp.append(list(map(lambda x: int(x) - 1, input().split())))
    dire.append(tmp)

def reduce_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j]:
                if smell[i][j][0] > 1:
                    smell[i][j][0] -= 1
                else:
                    smell[i][j] = []

def check_direction(x, y, s, d):
    global new_smell
    tmp = []
    for nd in dire[s][d]:
        nx, ny = x + dxy[nd][0], y + dxy[nd][1]
        if 0 <= nx < n and 0 <= ny < n:
            if smell[nx][ny] == []:
                shark[s] = [nx, ny, nd]
                if new_smell[nx][ny]:
                    del shark[new_smell[nx][ny][1]]
                new_smell[nx][ny] = [k + 1, s]
                return False
            elif smell[nx][ny][1] == s and tmp == []:
                tmp = [nx, ny, nd]

    return tmp

def deepcopy(arr):
    return [[a for a in ar] for ar in arr]

def move_shark():
    global new_smell
    new_smell = deepcopy(smell)
    # 상어의 INDEX가 뒷 숫자이면 덮어쓰기
    for s, val in sorted(shark.items(), reverse=True):
        x, y, d = val
        tmp = check_direction(x, y, s, d)
        if tmp:
            nx, ny, nd = tmp
            new_smell[nx][ny] = [k + 1, s]
            shark[s] = [nx, ny, nd]
    return new_smell


ans = 1
while ans <= 1000:
    smell = move_shark()
    reduce_smell()
    if len(shark) == 1:
        break
    ans += 1

print(ans if ans <= 1000 else -1)