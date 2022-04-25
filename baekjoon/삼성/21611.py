# 12:40 - 2:16
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

map_dict = {1: 3, 2: 1, 3: 0, 4: 2}

total_cnt = 0

dict = {}
dxy = [[0, -1], [1, 0], [0, 1], [-1, 0]]
def index_dict():
    cnt = 1
    k = 1
    d = 0
    x, y = n // 2, n // 2
    while cnt < n ** 2:
        t = 0
        while t < k:
            x += dxy[d][0]
            y += dxy[d][1]
            dict[cnt] = [x, y]
            t += 1
            cnt += 1
        if d == 1 or d == 3:
            k += 1
        d = (d + 1) % 4
    del dict[n ** 2]
index_dict()

def do_magic(d, s):
    x, y = n // 2, n // 2
    for _ in range(s):
        x += dxy[d][0]
        y += dxy[d][1]
        maps[x][y] = 0

from collections import deque
def explode_marble():
    q = deque()
    for _, v in dict.items():
        x, y = v
        if maps[x][y] != 0:
            q.append(maps[x][y])
    
    while True:
        isTrue, q = reduce_marble(q)
        if isTrue:
            return q
    

def reduce_marble(q):
    global total_cnt
    len_q = len(q)

    exploded = deque()
    val = -1
    cnt = 0 
    while q:
        ma = q.popleft()
        if val == ma:
            cnt += 1
        else:
            if cnt < 4:
                for _ in range(cnt):
                    exploded.append(val)
            else:
                total_cnt += (val * cnt)
            val = ma
            cnt = 1
    
    if cnt < 4:
        for _ in range(cnt):
            exploded.append(val)
    else:
        total_cnt += (val * cnt)

    if len_q != len(exploded):
        return False, exploded
    else:
        return True, exploded

def fill_marble(q):
    global maps
    maps = [[0] * n for _ in range(n)]
    if not q:
        return
    
    idx = 1
    val = q.popleft()
    cnt = 1
    while q and idx < n ** 2 - 1:
        while q and idx < n ** 2 - 1:
            t = q.popleft()
            if t == val:
                cnt += 1
            else:
                x, y = dict[idx]
                maps[x][y] = cnt
                idx += 1
                x, y = dict[idx]
                maps[x][y] = val
                idx += 1
                cnt = 1
                val = t
                break
    if idx < n ** 2 - 1:
        x, y = dict[idx]
        maps[x][y] = cnt
        idx += 1
        x, y = dict[idx]
        maps[x][y] = val

for _ in range(m):
    d, s = map(int,  input().split())
    d =  map_dict[d]
    do_magic(d, s)
    q = explode_marble()
    fill_marble(q)
    # print(maps)
print(total_cnt)