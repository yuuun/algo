#dp
n = int(input())
dp = [0] * (n + 1)
dp[1], dp[2] = 1, 3

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] * 2
print(dp[n] % 10007)