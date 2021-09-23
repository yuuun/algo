## backtracking
## https://www.acmicpc.net/problem/15650
n, m = map(int, input().split())
ans = []

def sol(depth, idx):
    if depth == m:
        print(' '.join(map(str, ans)))
    for i in range(idx + 1, n):
        ans.append(i + 1)
        sol(depth + 1, i)
        ans.pop()

sol(0, -1)