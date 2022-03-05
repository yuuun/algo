#순열 사이클
def dfs(x):
    visited[x] = True
    x = numbers[x]
    if not visited[x]:
        dfs(x)
    
for _ in range(int(input())):
    n = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    res = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            res += 1
    print(res)