n, k = map(int, input().split())
seq = [True if element % 2 == 0 else False for element in list(map(int, input().split()))]
dp = [[0] * (k + 1) for _ in range(n)]

for i in range(n):
    for j in range(k + 1):
        if seq[i]:
            dp[i][j] = dp[i - 1][j] + 1
        elif j != 0:
            dp[i][j] = dp[i - 1][j - 1]

ans = 0
for d in dp:
    ans = max(ans, max(d))
print(ans)