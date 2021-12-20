n, m = map(int, input().split())
nonice = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    nonice[a].append(b)
    nonice[b].append(a)

def dfs(selected, k):
    global s
    if k == 3:
        s += 1
        return
    for i in range(selected[-1] + 1, n + 1):
        if not candidate[i]:
            candidate[i] += 1
            for a in nonice[i]:
                candidate[a] += 1
            dfs(selected + [i], k + 1)
            candidate[i] -= 1
            for a in nonice[i]:
                candidate[a] -= 1

s = 0
candidate = [0] * (n + 1)
for i in range(1, n + 1):
    candidate[i] += 1
    for a in nonice[i]:
        candidate[a] += 1
    dfs([i], 1)
    candidate[i] -= 1
    for a in nonice[i]:
        candidate[a] -= 1
print(s)


## https://home-body.tistory.com/455