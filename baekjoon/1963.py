from collections import deque
n = int(input())
inp = []
max_val = 0
min_val = 9999
for _ in range(n):
    a, b = map(int, input().split())
    if b > max_val:
        max_val = b
    if a < min_val:
        min_val = a
    inp.append([a, b])

prime_list = [True] * 10000
for i in range(2, 101):
    if prime_list[i]:
        for j in range(i+i, 10000, i):
            prime_list[j] = False

def bfs(s, e):
    q = deque()
    q.append([s, 0])
    visited = [False for _ in range(10000)]
    visited[s] = 1
    while q:
        num, cnt = q.popleft()
        if num == e: 
            return cnt
        if num < 1000:
            continue
        for i in [1, 10, 100, 1000]:
            tmp = num - num % (i * 10) // i * i
            for _ in range(10):
                if not visited[tmp] and prime_list[tmp] and tmp > 1000:
                    visited[tmp] = True
                    q.append([tmp, cnt + 1])
                tmp += i

for a, b in inp:
    if a == b:
        print(0)
    else:
        res = bfs(a, b)
        if res == None:
            print("impossible")
        else:
            print(res)