# 시간초과
def solution2(food_times, k):
    cur = 0
    t = 0
    n = len(food_times)
    prev = n - 1
    visit = [True] * n
    next = {i: i + 1 for i in range(n - 1)}
    next[n - 1] = 0
    if k > sum(food_times):
        return -1
    while t < k:
        if food_times[cur] > 1:
            food_times[cur] -= 1
            prev = cur
            cur = next[cur]
        elif food_times[cur] == 1:
            food_times[cur] = 0
            # next[cur] = next[next[cur]]
            next[prev] = next[cur]
            del next[cur]
            visit[cur] = False
            cur = next[prev]
        t += 1
    if visit[cur]:
        return cur + 1
    else:
        k = 1
        while True:
            nx = cur - k
            if visit[nx]:
                return nx + 1
            nx = cur + k
            if visit[nx]:
                return nx + 1
            k += 1

from collections import defaultdict
def solution(food_times, k):
    if k >= sum(food_times):
        return -1
    dic = defaultdict(list)
    for i, food in enumerate(food_times):
        dic[food].append(i)
    t, repeated = 0, 1
    n = len(food_times)
    visited = [True] * n
    while t <= k - n:
        t += n
        for idx in dic[repeated]:
            visited[idx] = False
            n -= 1
        repeated += 1
    t = k - t
    cur = 0
    while t > -1:
        while not visited[cur]:
            cur += 1
        cur += 1
        t -= 1
    if cur > 0:
        cur -= 1
    if visited[cur]:
        return cur + 1
    k = 1
    while True:
        nx = cur - k
        if visited[nx]:
            return nx + 1
        nx = cur + k
        if visited[nx]:
            return nx + 1
        k += 1
        
# print(solution([3, 1, 2], 5), 1)
print(solution([4,2,3,6,7,1,5,8], 16))
print(solution2([4,2,3,6,7,1,5,8], 27))