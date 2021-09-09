n = int(input())
a = list(map(int, input().split()))

dp = [a[0]]
for i in range(n - 1):
    dp.append(max(dp[i] + a[i + 1], a[i + 1]))
print(max(dp))