import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

start, end = 0, 1
n1 = nums[start: end + 1]
n2 = nums[end: start]

'''
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

start = 0
end = 1

cnt = 0
while True:
    if end > n:
        break
    if start == 0:
        lst1 = lst[:end+1:1]
        lst2 = lst[end::-1]
    else:
        lst1 = lst[start:end+1:1]
        lst2 = lst[end:start-1:-1]
    if lst1 == lst2:
        cnt += 1
        start = end + 1
        end = start + 1
    else:
        end += 2

print(cnt) if start == n else print(-1)

'''

'''
import sys
n = int(sys.stdin.readline())
num = [0] + list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][i] = 1
    for j in range(i - 1, 0, -1):
        if j == i - 1 and num[j] == num[i]:
            dp[j][i] = 1
        elif num[i] == num[j] and dp[j + 1][i - 1] == 1:
            dp[j][i] = 1
ans = [-1] * (n + 1)
for i in range(2, n + 1, 2):
    if dp[1][i] == 1:
        ans[i] = 1
    for j in range(2, i - 1, 2):
        if ans[j] != -1 and dp[j + 1][i] == 1:
            ans[i] = max(ans[i], ans[j] + 1)
print(ans[-1])
'''