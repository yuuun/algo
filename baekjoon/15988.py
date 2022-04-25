dp = [1, 2, 4]
l = 3
for _ in range(int(input())):
    t = int(input())
    while t > l:
        dp.append((dp[l - 1] + dp[l - 2] + dp[l - 3]) %1000000009)
        l += 1
    print(dp[-1])