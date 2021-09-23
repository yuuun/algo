## backtracking
## https://www.acmicpc.net/problem/15654
n, m = map(int, input().split())
com = sorted(list(map(int, input().split())))
ans = []

def sol(depth):
    if depth == m:
        print(' '.join(map(str, ans)))
        return ans
    for i in range(n):
        if com[i] not in ans:
            ans.append(com[i])
            sol(depth + 1)
            ans.pop()
sol(0)
