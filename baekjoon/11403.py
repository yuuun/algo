from collections import defaultdict, deque
n = int(input())
maps = []
dic = defaultdict(list)
for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(n):
        if maps[i][j] == 1:
            dic[i].append(j)

def fill_maps(x):
    arr = [0] * n
    q = deque([x])
    while q:
        t = q.popleft()
        for k in dic[t]:
            if arr[k] == 0:
                arr[k] = 1
                q.append(k)
    return arr

for i in range(n):
    print(' '.join(map(str, fill_maps(i))))