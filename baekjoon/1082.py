n = int(input())
arr = list(map(int, input().split()))
m = int(input())
dp = [0 for _ in range(m + 1)]
for i in range(n - 1, -1, -1):
    x = arr[i]
    for j in range(x, m + 1):
        dp[j] = max(dp[j - x] * 10 + i, i, dp[j])
print(dp[-1])