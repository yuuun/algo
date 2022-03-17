n, m = int(input()), int(input())
dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]
arr = [[1] * n for _ in range(n)]

k = n // 2
x, y = k, k
cnt, idx = 1, 2
map_size = n ** 2
while idx < map_size:
    for i in range(4):
        t = 0
        while t < cnt and idx < map_size:
            x += dxy[i][0]
            y += dxy[i][1]
            arr[x][y] = idx
            idx += 1
            t += 1
        if i in [1, 3]:
            cnt += 1
arr[0][0] = map_size
for i, a in enumerate(arr):
    print(' '.join(map(str, a)))
    if m in a:
        x, y = i + 1, a.index(m) + 1
print(x, y)