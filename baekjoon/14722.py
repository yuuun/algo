n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n + 1)]

dic = {0: 2, 1: 0, 2: 1}
dp[1][1] = 1
for j in range(2, n + 1):
    if dic[adj[0][j - 1]] == adj[0][j - 2]:
        dp[1][j - 1] = dp[1][j - 2] + 1
    else:
        dp[1][j - 1] = dp[1][j - 2]

for i in range(2, n + 1):
    if dic[adj[i - 1][0]] == adj[i - 2][0]:
        dp[i - 1][1] = dp[i - 2][1] + 1
    else:
        dp[i - 1][1] = dp[i - 2][1]

max_val = 0
for i in range(2, n + 1):
    for j in range(2, n + 1):
        tmp = [dp[i][j - 1], dp[i - 1][j]]
        if dic[adj[i - 1][j - 1]] == adj[i - 1][j - 2]:
            tmp.append(dp[i][j - 1] + 1)
        if dic[adj[i - 1][j - 1]] == adj[i - 2][j - 1]:
            tmp.append(dp[i - 1][j] + 1)
        dp[i][j] = max(tmp)
        max_val = max(dp[i][j], max_val)
print(max_val)