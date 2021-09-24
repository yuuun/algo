## backtracking
## https://www.acmicpc.net/problem/15652
n, m = map(int, input().split())
ans = []

def sol(depth, idx):
    if depth == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(idx, n):
        ans.append(i + 1)
        sol(depth + 1, i)
        ans.pop()

sol(0, 0)