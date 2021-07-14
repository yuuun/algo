n, k = map(int, input().split())
c = [int(input()) for _ in range(n)]

dp = [0 for i in range(k + 1)]
dp[0] = 1

for i in c:
    for j in range(i, k + 1):
        tmp = j - i
        if tmp >= 0:
            dp[j] += dp[tmp]
print(dp[k])