# 30 분 소요
from collections import deque
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

def find_start():
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 9:
                maps[i][j] = 0
                return i, j

sx, sy = find_start()
size = 2
ans = 0
n_eat = 0

dxy = [[-1, 0], [0, -1], [1, 0], [0, 1]]

def is_criteria(r, c):
    if 0 <= r < n and 0 <= c < n:
        return True 
    return False

from heapq import heappop, heappush
while True:
    q = deque()
    q.append([sx, sy, 0])
    visited = [[False] * n for _ in range(n)]
    fish = []
    
    while q:
        x, y, dist = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
						# 이동 가능한 위치 탐색
            if is_criteria(nx, ny) and size >= maps[nx][ny] and not visited[nx][ny]:
                if maps[nx][ny] != 0 and size > maps[nx][ny]:
                    # fish.append([nx, ny, dist + 1])
                    heappush(fish, [dist + 1, nx, ny])
                visited[nx][ny] = True
                q.append([nx, ny, dist + 1])
    
		# 먹은 물고기의 개수와 자신의 몸 크기를 비교하여 물고기의 크기를 키워주는지 확인
    if len(fish) > 0:
        dis, x, y = heappop(fish)
    
        ans += dis
        n_eat += 1
        maps[x][y] = 0
        
        if n_eat == size:
            size += 1
            n_eat = 0
        sx, sy = x, y
    else:
        break

print(ans)