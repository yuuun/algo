from collections import deque
n, k = map(int, input().split())
MAX = 100000
visited = [[-1, 0] for _ in range(MAX + 1)]

q = deque([n])
visited[n][0] = 0
visited[n][1] = 1

while q:
    cur = q.popleft()
    for x in [cur - 1, cur + 1, 2 * cur]:
        if 0 <= x <= MAX:
            if visited[x][0] == -1: # 최초 도착
                visited[x][0] = visited[cur][0] + 1
                visited[x][1] = visited[cur][1]
                q.append(x)
            
            elif visited[x][0] == visited[cur][0] + 1:
                visited[x][1] += visited[cur][1]

print(visited[k][0])
print(visited[k][1])