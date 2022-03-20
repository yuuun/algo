n = int(input())

dp = [0] * (n + 1)
dp[0] = 1
num = 1
while num <= n:
    for j in range(num, n + 1):
        dp[j] += dp[j - num]
    num *= 2
print(dp)

print(dp[-1] % 1000000000)