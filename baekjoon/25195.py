import sys
sys.setrecursionlimit(10**5)
from collections import defaultdict
n, m = map(int, input().split())
dic = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
S = int(input())
arr = list(map(int, input().split()))
start = 1

def dfs(idx):
    global isTrue
    if not dic[idx]:
        print('yes')
        exit()
    for i in dic[idx]:
        if i not in arr:
            dfs(i)


if start in arr:
    print('Yes')
    exit()
dfs(start)
print('Yes')