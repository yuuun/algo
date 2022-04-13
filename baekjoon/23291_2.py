n, k = map(int, input().split())
fishes = list(map(int, input().split()))
n_2 = n // 2
n_4 = n // 4

def rotate90(arr):
    return [list(ar) for ar in zip(*arr[::-1])]

def add_min():
    min_val = min(fishes)
    for i in range(len(fishes)):
        if fishes[i] == min_val:
            fishes[i] += 1

def flatten(arr):
    tmp = []
    for j in range(len(arr[0])):
        for i in range(len(arr) - 1, -1, -1):
            tmp.append(arr[i][j])
    return tmp

def find_sub():
    arr = sorted(fishes)
    return arr[-1] - arr[0]

def snail():
    global fishes
    add_min()
    left, right = [[fishes[0]], [fishes[1]]], fishes[2:]
    z = 2
    left = rotate90(left) + [right[:2]]
    right = right[2:]
    i = 0
    while True:
        left = rotate90(left) + [right[:z]]
        right = right[z:]
        if i % 2 == 1:
            z += 1
        if len(right) < z:
            break

        i += 1
    
    add_left = [[0] * len(left[0]) for _ in range(len(left))]
    for x in range(len(left) - 1):
        for y in range(len(left[x]) - 1):
            for dx, dy in [[0, 1], [1, 0]]:
                nx, ny = x + dx, y + dy
                sub = int((left[nx][ny] - left[x][y]) / 5)
                if sub != 0:
                    add_left[nx][ny] -= sub
                    add_left[x][y] += sub
    
    for x in range(len(left) - 1):
        nx = x + 1
        sub = int((left[nx][-1] - left[x][-1]) / 5)
        if sub != 0:
            add_left[nx][-1] -= sub
            add_left[x][-1] += sub
    for y in range(len(left[0]) - 1):
        ny = y + 1
        sub = int((left[-1][ny] - left[-1][y]) / 5)
        if sub != 0:
            add_left[-1][ny] -= sub
            add_left[-1][y] += sub
    
    if right:
        add_right = [0] * len(right)
        sub = int((left[-1][-1] - right[0]) / 5)
        if sub != 0:
            add_left[-1][-1] -= sub
            add_right[0] += sub
        
        for i, j in zip(range(len(right)), range(1, len(right))):
            sub = int((right[j] - right[i]) / 5)
            if sub != 0:
                add_right[j] -= sub
                add_right[i] += sub
        for i in range(len(right)):
            right[i] += add_right[i]
    
    for x in range(len(left)):
        for y in range(len(left[0])):
            left[x][y] += add_left[x][y]

    fishes = flatten(left) + right
    
    fishes = [fishes[:n_2][::-1]] + [fishes[n_2:]]
    left = []
    right = []
    for i in range(len(fishes)):
        left.append(fishes[i][:n_4])
        right.append(fishes[i][n_4:])
    left = rotate90(rotate90(left))
    fishes = left + right

    add_cnt = [[0] * n_4 for _ in range(n_2)]

    for x in range(n_2):
        for y in range(n_4):
            for dx, dy in [[0, 1], [1, 0]]:
                nx, ny = x + dx, y + dy
                if nx < n_2 and ny < n_4:
                    sub = int((fishes[nx][ny] - fishes[x][y]) / 5)
                    if sub != 0:
                        add_cnt[nx][ny] -= sub
                        add_cnt[x][y] += sub
    
    for x in range(n_2):
        for y in range(n_4):
            fishes[x][y] += add_cnt[x][y]
    
    fishes = flatten(fishes)

cnt = 1
while True:
    snail()
    print(fishes)
    if find_sub() <= k:
        print(cnt)
        break

    cnt += 1