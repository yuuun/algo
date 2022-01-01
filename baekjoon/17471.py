from collections import defaultdict
n = int(input())

population = list(map(int, input().split()))

loc = defaultdict(set)
for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    for t in tmp[1:]:
        loc[i].add(t)
        loc[t].add(i)
print(loc)