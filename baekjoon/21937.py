from collections import defaultdict, deque
n, m = map(int, input().split())
dic = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    dic[b].append(a)

x = int(input())
visited = [False] * (n + 1)
q = deque()
q.append(x)
ans = 0

while q:
    x = q.popleft()
    for b in dic[x]:
        if not visited[b]:
            visited[b] = True
            q.append(b)
            ans += 1
print(ans)