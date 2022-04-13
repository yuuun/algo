from collections import deque

n = int(input())
k = int(input())
visited = [[False] * n for _ in range(n)]
visited[0][0] = True
maps = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(lambda x: int(x) - 1, input().split())
    maps[x][y] = 1

l = int(input())
order = {}
for _ in range(l):
    x, c = input().split()
    order[int(x)] = c

dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]] # 상 우 하 좌
dir_left = {0:3, 3:2, 2:1, 1:0}
dir_right = {0:1, 1:2, 2:3, 3:0}
d = 1

cnt = 1
q = deque([[0, 0]])
x, y = 0, 0
while True:
    x, y = x + dxy[d][0], y + dxy[d][1]
    if 0 <= x < n and 0 <= y < n and not visited[x][y]:
        if maps[x][y] == 0: #사과가 없는 경우
            tx, ty = q.popleft()
            visited[tx][ty] = False
        else:
            maps[x][y] = 0
        visited[x][y] = True
        q.append([x, y])
        
        if cnt in order.keys():
            if order[cnt] == 'L':
                d = dir_left[d]
            else:
                d = dir_right[d]
        cnt += 1
            
    else:
        print(cnt)
        exit()
    