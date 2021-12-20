import sys
sys.setrecursionlimit(10**9)
n = int(input())

dic = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)
parent = [0] * (n + 1)

def sol(i, dic, parent):
    for lin in dic[i]:
        if parent[lin] == 0:
            parent[lin] = i
            sol(lin, dic, parent)

sol(1, dic, parent)

for i in parent[2:]:
    print(i)