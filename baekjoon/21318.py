import sys
input = sys.stdin.readline
n = int(input())
hard = list(map(int, input().split()))
dp = [0]
for i, j in zip(range(n), range(1, n)):
    if hard[j] < hard[i]:
        dp.append(dp[-1])
    else:
        dp.append(1 + dp[-1])

dp.append(1 + dp[-1])

for _ in range(int(input())):
    x, y = map(int, input().split())
    print(y - x - (dp[y - 1] - dp[x - 1]))