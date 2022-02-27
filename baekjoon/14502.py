from collections import deque
n, m = map(int, input().split())
virus = []
maps = []
walls = []

# 바이러스가 있는 위치 매번 재사용하기 때문에 저장
for i in range(n):
    tmp = list(map(int, input().split()))
    for j, t in enumerate(tmp):
        if t == 2:
            virus.append([i, j])
        if t == 1:
            walls.append([i, j])
    maps.append(tmp)

def check_map(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
n_zero = n * m - len(virus) - len(walls) - 3

def get_visited():
    visited = [[False] * m for _ in range(n)]
    for i, j in virus + walls:
        visited[i][j] = True
    return visited

# bfs
def spread_virus():
    global ans, n_zero
    visited = get_visited()
    q = deque(virus)
    n_zeros = n_zero
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if check_map(nx, ny) and not visited[nx][ny]:
                if maps[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    n_zeros -= 1
    ans = max(ans, n_zeros)

# dfs
def make_wall(cnt, row, col):
    if cnt == 3:
        spread_virus()
        return
    for i in range(row, n):
        for j in range(col, m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                make_wall(cnt + 1, i, j + 1)
                maps[i][j] = 0
        col = 0

ans = 0
make_wall(0, 0, 0)
print(ans)


''' 시간 제일 짧게 걸린 것
from itertools import combinations
N,M = map(int,input().split())
org_box = [list(map(int,input().split())) for _ in range(N)]
# 울타리 세울 수 있는 곳 찾기
def get_zero_pos(v_map):
    zero_pos_list = []
    for i in range(N):
        for j in range(M):
            if v_map[i][j] == 0:
                zero_pos_list.append((i,j))
    return zero_pos_list
def use_stack(N,M,org_box) :
#     space = [(n, m) for n in range(N) for m in range(M) if not org_box[n][m]]
#     def f(pair) :
#         y,x = pair
#         return sum(True for n,m in ((0,1),(0,-1),(1,0),(-1,0)) if not 0<=y+n<N or not 0<=x+m<M or org_box[y+n][x+m])
#     space.sort(key=f,reverse=True)
    space = get_zero_pos(org_box)
    virus = [(n, m) for n in range(N) for m in range(M) if org_box[n][m] == 2]
    S = len(space)

    result = -1
    ct = 0
    for pair in combinations(range(S), 3):
        ct += 1
        box = [b[:] for b in org_box]
        for d in pair:
            y, x = space[d]
            box[y][x] = 1
        stack = [(n, m) for n, m in virus]
        count = S - 3
        while stack:
            y, x = stack.pop()
            if count < result: break
            for n, m in (0, 1), (-1, 0), (0, -1), (1, 0):
                if 0 <= y + n < N and 0 <= x + m < M and not box[y + n][x + m]:
                    box[y + n][x + m] = 2
                    count -= 1
                    stack.append((y + n, x + m))
        result = max(result, count)
#     print(ct)
    return result

# print(use_stack(n,m,data))
print(use_stack(N,M,org_box))

'''