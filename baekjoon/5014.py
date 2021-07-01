from collections import deque
f, s, g, u, d = map(int, input().split())

visited = [False for _ in range(f + 1)]

cnt = 0
q = deque([[s, 0]])
while q:
    cur, cnt = q.popleft()
    if not visited[cur]:
        if cur == g:
            break
        visited[cur] = True
        if cur + u <= f:
            q.append([cur + u, cnt + 1])
        if cur - d > 0:
            q.append([cur - d, cnt + 1])

if cur != g:    
    print('use the stairs')
else:
    print(cnt)