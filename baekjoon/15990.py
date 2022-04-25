MOD = 1000000009
dp = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
for _ in range(int(input())):
    t = int(input())
    for i in range(len(dp), t):
        dp.append([(dp[-1][2] + dp[-1][1]) % MOD, (dp[-2][0] + dp[-2][2]) % MOD, (dp[-3][0] + dp[-3][1]) % MOD])
    print(sum(dp[t-1]) % MOD)
    