n, k = map(int, input().split())
c = [int(input()) for _ in range(n)]

dp = [0 for i in range(k + 1)]
for i in range(1, k + 1):
    tmp = []
    for j in c:
        if j <= i and dp[i - j] != -1:
            tmp.append(dp[i - j])
    if not tmp:
        dp[i] = -1
    else:
        dp[i] = min(tmp) + 1
print(dp[k])