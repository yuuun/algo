from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    t = n + 2
    
    inp = [list(map(int, input().split())) for _ in range(t)]
    edges = [[] for _ in range(t)]
    adj = [[0] * t for _ in range(t)]

    for i in range(t):
        for j in range(t):
            if i != j and abs(inp[i][0] - inp[j][0]) + abs(inp[i][1] - inp[j][1]) <= 1000:
                edges[i].append(j)
                
    visited = [False for _ in range(t)]
    q = deque()
    q.append(0)
    while q:
        cur = q.popleft()
        for i in edges[cur]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                
    if visited[n + 1]:
        print("happy")
    else:
        print("sad")