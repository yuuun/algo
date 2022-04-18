## 2, 7
from collections import deque
maps = [deque(list(input())) for _ in range(4)]

def rotate_right(c, d):
    if c == 4:
        return
    if maps[c - 1][2] != maps[c][6]:
        rotate_right(c + 1, -d)
        maps[c].rotate(d)
    else:
        return

def rotate_left(c, d):
    if c == -1:
        return
    if maps[c + 1][6] != maps[c][2]:
        rotate_left(c - 1, -d)
        maps[c].rotate(d)
    else:
        return

for _ in range(int(input())):
    c, d = map(int, input().split())
    rotate_right(c, -d)
    rotate_left(c - 2, -d)
    maps[c - 1].rotate(d)

ans = 0
for i in range(4):
    if maps[i][0] == '1':
        ans += 1 << i
print(ans)