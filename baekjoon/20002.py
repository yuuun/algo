import sys
input = sys.stdin.readline
n = int(input())
apple = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        apple[i][j] += apple[i][j - 1]
for j in range(1, n + 1):
    for i in range(1, n + 1):
        apple[i][j] += apple[i - 1][j]
'''
dp = [[0] * (n + 1) for _ in range(n + 1)]
apple = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + apple[i][j]
'''

max_val = -200000000
for k in range(1, n + 1):
    for i in range(n + 1 - k):
        i2 = i + k
        for j in range(n + 1 - k):
            j2 = j + k
            max_val = max(max_val, apple[i2][j2] + apple[i][j] - apple[i][j2] - apple[i2][j])
print(max_val)