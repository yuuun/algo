r, c = map(int, input().split())
loc = []
for _ in range(r):
    st = input()
    loc.append([s for s in st])

ans = 0
dy = [-1, 0, 1]

def connect(y, x):
    if x == c - 1:
        return True

    loc[y][x] = 'x'
    
    nx = x + 1
    for dys in dy:
        ny = y + dys
        if 0 <= ny < r and 0 <= nx < c and loc[ny][nx] == '.':
            if connect(ny, nx):
                return True
    return False

for i in range(r):
    if connect(i, 0):
        ans += 1
print(ans)