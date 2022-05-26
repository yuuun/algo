from collections import deque, defaultdict
n, m = map(int, input().split())
maps = []
check_node = defaultdict(int)
cnt = 0
locs = []
for i in range(n):
    tmp = list(input())
    for j in range(n):
        if tmp[j] in ['S', 'K']:
            check_node[(i, j)] = cnt
            cnt += 1
            locs.append([i, j])
    maps.append(tmp)

dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
q = deque()
edge = []
for x, y in locs:
    q.append([x, y])
    check = [[-1] * n for _ in range(n)]
    check[x][y] = 0
    while q:
        _x, _y = q.popleft()
        for dx, dy in dxy:
            nx, ny = _x + dx, _y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] != '1':
                    if check[nx][ny] == -1:
                        check[nx][ny] = check[_x][_y] + 1
                        q.append([nx, ny])
    for tx, ty  in locs:
        if check[tx][ty] > 0:
            edge.append([check[tx][ty], check_node[(x, y)], check_node[(tx, ty)]])

parents = [i for i in range(m + 1)]
def find_parent(x):
    if parents[x] != x:
        parents[x] = find_parent(parents[x])
    return parents[x]

def union_parent(x, y):
    x, y = find_parent(x), find_parent(y)
    parents[y] = x

edge.sort()
mst = 0
res = 0
for ch, x, y in edge:
    if res == m:
        break
    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        res += 1
        mst += ch
print(mst if res == m else -1)