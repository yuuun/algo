#시간초과
from itertools import combinations
from collections import defaultdict
n = int(input())

dots = []
for _ in range(n):
    dots.append(list(map(int, input().split())))

def chck(a, b):
    if a[0] * b[0] + a[1] * b[1] == 0:
        return True

def sub(a, b):
    return [a[0] - b[0], a[1] - b[1]]

cnt = 0
for x, y, z in combinations(dots, 3):
    xs, ys, zs = sub(x, y), sub(y, z), sub(z, x)
    if chck(xs, ys):
        cnt += 1
        continue
    if chck(ys, zs):
        cnt += 1
        continue
    if chck(zs, xs):
        cnt += 1
        continue
print(cnt)
     
'''
row = defaultdict(list) 
col = defaultdict(list)
idx = 0
for _ in range(n):
    x, y = map(int, input().split())
    row[x].append([y, idx])
    col[y].append([x, idx])
    idx += 1


for k, vs in row.items():
    if len(vs) > 1: 
        for i1 in range(len(vs)):
            v1 = vs[i1][1]
            for i2 in range(i1 + 1, len(vs)):
                v2 = vs[i2][1]
                can = set([v1, v2])
                
'''