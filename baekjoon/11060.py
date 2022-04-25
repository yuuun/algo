n = int(input())
maps = list(map(int, input().split()))
dp = [2000] * n
dp[0] = 0
for i in range(n):
    for j in range(1, maps[i] + 1):
        if i + j >= n:
            break
        dp[i + j] = min(dp[i + j], dp[i] + 1)
print(dp[-1] if dp[-1] != 2000 else -1)