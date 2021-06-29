from collections import deque
n, k = map(int, input().split())

visited = [False] * 100001
cnt = 0

queue = deque([[n, cnt]])
while queue:
    cur, cnt = queue.popleft()
    if not visited[cur]:
        visited[cur] = True
        if cur == k:
            break
        if cur * 2 <= 100000:
            queue.append([2 * cur, cnt + 1])
        if cur - 1 >= 0:
            queue.append([cur - 1, cnt + 1])
        if cur + 1 <= 100000:
            queue.append([cur + 1, cnt + 1])

print(cnt)  