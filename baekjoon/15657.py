## backtracking
## https://www.acmicpc.net/problem/15657

n, m = map(int, input().split())
com = sorted(list(map(int, input().split())))
ans = []

def sol(depth, idx):
    if depth == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(idx, n):
        ans.append(com[i])
        sol(depth + 1, i)
        ans.pop()

sol(0, 0)