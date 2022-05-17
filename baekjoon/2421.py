MAX_SIZE = 1000000
n = int(input())
dp = [[0] * (n + 1) for _ in range(n + 1)]
prime = [1] * MAX_SIZE # 1일 때, 소수

for i in range(2, MAX_SIZE):
    for j in range(i * i, MAX_SIZE, i):
        prime[j] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + prime[int(str(i) + str(j))]
print(dp[n][n] - 1)