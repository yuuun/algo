dic = {}
idx = 0
n = int(input())
for _ in range(n):
    dic[input()] = idx
    idx += 1

visited = [False] * n
i = 0
ans = 0
chk = []
for _ in range(n):
    t = dic[input()]
    chk.append(t)
    visited[t] = True
    if i != t:
        ans += 1
    else:
        while i < n and visited[i]:
            i += 1
print(ans)