n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]
'''
d = [[1, 0], [0, 1]]

cnt = 0
###dfs: 시간 초과..!

def dfs(x, y):
    global cnt
    if adj[x][y] == 0:
        cnt += 1
        return
    for dx, dy in d:
        tx = x + adj[x][y] * dx
        ty = y + adj[x][y] * dy
        if 0 <= tx < n and 0 <= ty < n:
            dfs(tx, ty)

dfs(0, 0)
print(cnt)
'''
mov = [[0] * n for _ in range(n)]
mov[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(mov[i][j])
            break
        cur = adj[i][j]
        tj = j + cur
        ti = i + cur
        if tj < n:
            mov[i][tj] += mov[i][j]
        if ti < n:
            mov[ti][j] += mov[i][j]