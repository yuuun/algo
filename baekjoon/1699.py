#https://pacific-ocean.tistory.com/205
import math
n = int(input())
dp = [0] * (n + 1)
sqr = [i * i for i in range(1, int(math.sqrt(n + 1)) + 1)]

for i in range(1, n + 1):
    tmp = []
    for j in sqr:
        if j > i:
            break
        tmp.append(dp[i - j])
    dp[i] = min(tmp) + 1
print(dp[n])