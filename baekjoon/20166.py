dxy = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

n, m, k = map(int, input().split())
maps = [list(input()) for _ in range(n)]
def dfs(depth, cur, x, y):
    global len_match, cnt, match
    if len_match == depth:
        cnt += 1
        return
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        nx %= n
        ny %= m
        if match[depth] == maps[nx][ny]:
            dfs(depth + 1, cur + maps[nx][ny], nx, ny)

for _ in range(k):
    cnt = 0
    match = input()
    len_match = len(match)
    for x in range(n):
        for y in range(m):
            if maps[x][y] == match[0]:
                dfs(1, maps[x][y], x, y)
    print(cnt)

'''
import sys
from collections import defaultdict as dd
input = sys.stdin.readline

n, m, k = map(int, input().split())

raw = [input().rstrip() for _ in range(n)]

board = ''.join(raw)
cnt = 0
dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
q = dd(lambda :dd(list))

for i in range(n*m):
    q[-1][board[i]].append(i)

for i in range(n):
    for j in range(m):
        ij = i*m+j
        for dx, dy in dir:
            i0 = (i + dx) % n
            j0 = (j + dy) % m
            ij0 = i0*m+j0
            q[ij][board[ij0]].append(ij0)

save = {(i, 0): 1 for i in range(n*m)}

def get_hash(s : str):
    ans = 0
    for c in s:
        ans = ans * 27 + ord(c) - 96
    return ans

def get_ans(start: int, d: int, hashed: int) -> int:
    if (start, hashed) in save:
        return save[start, hashed]
    ans = 0
    d -= 1
    new_hashed = hashed // 27
    for nxt in q[start][god[d]]:
        ans += get_ans(nxt, d, new_hashed)
    save[start, hashed] = ans
    return ans

for _ in range(k):
    god = input().rstrip()
    print(get_ans(-1, len(god), get_hash(god)))




'''