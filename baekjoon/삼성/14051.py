n = int(input())
n_1 = n + 1
dp = [0] * n_1
for i in range(n):
    d, s = map(int, input().split())
    if i + d < n_1:
        dp[i] += s
    for j in range(i + d, n_1):
        dp[j] = max(dp[j], dp[i])

print(dp[-1])