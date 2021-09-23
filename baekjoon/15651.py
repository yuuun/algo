## backtracking
## https://www.acmicpc.net/problem/15651

n, m = map(int, input().split())
ans = []

def sol(depth):
    if depth == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(n):
        ans.append(i + 1)
        sol(depth + 1)
        ans.pop()
sol(0)