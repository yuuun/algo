n = int(input())
maps = []
for _ in range(n):
    a, b = map(int, input().split())
    maps.append([a, abs(b)])
maps = sorted(maps)
dp = [1e20] * (n + 1)
dp[0] = 0
dp[1] = maps[0][1] * 2

for i in range(1, n):
    h = maps[i][1]
    for j in range(i, -1, -1):
        h = max(h, maps[j][1])
        dp[i + 1] = min(dp[i + 1], max(2 * h, maps[i][0] - maps[j][0]) + dp[j])
print(dp[-1])