n = int(input())
adj = [input() for _ in range(n)]
d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

x, y = 0, 0

def dfs(x, y):
    global cnt
    adj[x] = adj[x][:y] + "0" + adj[x][y+1:]
    cnt += 1
    for dx, dy in d:
        tx, ty = x + dx, y + dy
        if 0 <= tx < n and 0 <= ty < n:
            if adj[tx][ty] == "1":
                dfs(tx, ty)

ans = []

for i in range(n):
    for j in range(n):
        if adj[i][j] == '1':
            cnt = 0
            dfs(i, j)
            ans.append(cnt)
print(len(ans))
print('\n'.join(map(str, sorted(ans))))