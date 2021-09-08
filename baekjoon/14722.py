#TBD
n = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dic = {0: 2, 1: 0, 2: 1}
dp[0][0] = 1
for i in range(1, n):
    if dic[adj[i][0]] == adj[i - 1][0]:
        dp[i][0] = dp[i - 1][0] + 1
    else:
        dp[i][0] = dp[i - 1][0]

for j in range(1, n):
    if dic[adj[0][j]] == adj[0][j - 1]:
        dp[0][j] = dp[0][j - 1] + 1
    else:
        dp[0][j] = dp[0][j - 1]
        
max_val = 0
for i in range(1, n):
    for j in range(1, n):
        tmp = [dp[i][j - 1], dp[i - 1][j]]
        val = dic[adj[i][j]]
        if val == adj[i][j - 1]:
            tmp.append(dp[i][j - 1] + 1)
        if val == adj[i - 1][j]:
            tmp.append(dp[i - 1][j] + 1)
        dp[i][j] = max(tmp)
        max_val = max(dp[i][j], max_val)
print(dp)