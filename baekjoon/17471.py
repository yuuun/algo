from collections import defaultdict, deque
from itertools import combinations
import sys

n = int(input())

population = [0] + list(map(int, input().split()))

loc = defaultdict(set)
for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    for t in tmp[1:]:
        loc[i].add(t)

def is_graph(candidate):
    q = deque()
    visited = [False] * (n + 1)
    q.append(candidate[0])
    visited[candidate[0]] = True
    while q:
        k = q.popleft()
        for i in loc[k]:
            if i not in candidate:
                continue
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return visited.count(True) == len(candidate)
    
def sum_up(candidate):
    ans = 0
    for can in candidate:
        ans += population[can]
    return ans


min_value = sys.maxsize
# 5개의 구역을 (2, 3)으로 나누는 것과 (3, 2)로 나누는 것이 동일
for i in range(1, n // 2 + 1): 
    comb = list(combinations(range(1, n + 1), i))
    for com in comb:
        com = set(com)
        com2 = list(set(range(1, n + 1)).difference(com))
        com = list(com)
        # print(com, is_graph(com), com2, is_graph(com2))
            
        if is_graph(com):
            if is_graph(com2):
                min_value = min(min_value, abs(sum_up(com) - sum_up(com2)))
if min_value == sys.maxsize:
    print(-1)
else:
    print(min_value)
