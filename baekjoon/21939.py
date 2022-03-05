from heapq import heappop, heappush, heapify
import sys
input = sys.stdin.readline
n = int(input())

visited = {}
min_heap = []
max_heap = []
# heap는 최대값 찾기가 불가능하기 때문에 두 종류의 heap필요
for _ in range(n):
    x, y = map(int, input().split())
    min_heap.append([y, x])
    max_heap.append([-y, -x])
    visited[x] = True
heapify(min_heap)
heapify(max_heap)

def check_max_heap():
    global max_heap
    while not visited[-max_heap[0][1]]:
        heappop(max_heap)

def check_min_heap():
    global min_heap
    while not visited[min_heap[0][1]]:
        heappop(min_heap)

m = int(input())
for _ in range(m):
    commands = list(map(str, input().split()))
    if commands[0] == 'add':
        x, y = map(int, commands[1:])
        heappush(max_heap, [-y, -x])
        heappush(min_heap, [y, x])
        visited[x] = True
    elif commands[0] == 'recommend':
        if commands[1] == '1':
            print(-max_heap[0][1])
        else:
            print(min_heap[0][1])
    else:
        visited[int(commands[1])] = False
        check_max_heap()
        check_min_heap()