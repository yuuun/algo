from heapq import heappush, heappop
from collections import defaultdict

def solution(operations):
    positive_heap = []
    negative_heap = []
    visited = defaultdict(int)
    for instruction in operations:
        ins, num = instruction.split()
        n = int(num)
        if ins == 'I':
            heappush(positive_heap, n)
            heappush(negative_heap, -n)
            visited[n] = 1
        else:
            if n == -1:
                if len(positive_heap) == 0:
                    continue
                t = heappop(positive_heap)
                if t in visited:
                    while visited[t] == 0:
                        if len(positive_heap) == 0:
                            break
                        t = heappop(positive_heap)
                visited[t] = 0
            else:
                if len(negative_heap) == 0:
                    continue
                t = -heappop(negative_heap)
                if t in visited:
                    while visited[t] == 0:
                        if len(negative_heap) == 0:
                            break
                        t = heappop(negative_heap)
                visited[t] = 0
    
    answer = []
    for key, value in visited.items():
        if value == 1:
            answer.append(key)
    
    if len(answer) == 0:
        return [0, 0]
    else:
        return [max(answer), min(answer)]
    
print(solution(["I 16","D 1"])) # [0, 0]
print(solution(["I 7","I 5","I -5","D -1"])) # [7, 5]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])) # [333, -45]
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])) # [0, 0]