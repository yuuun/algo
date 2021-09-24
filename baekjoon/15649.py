## backtracking
## https://www.acmicpc.net/problem/15649

n, m = map(int, input().split())
visited = [False] * n
ans = []

def sol(depth):
    if depth == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            ans.append(i + 1)
            sol(depth + 1)
            visited[i] = False  # 깊이 탐사 완료
            ans.pop()

sol(0)