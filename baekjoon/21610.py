'''
n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
def get_cloud(cloud):
    global maps
    new_cloud = []
    for i in range(n):
        for j in range(n):
            if maps[i][j] > 1 and not visited[i][j]:
                new_cloud.append([i, j])
                maps[i][j] -= 2
    return new_cloud

direction = [[], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
cloud_dir = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
for _ in range(m):
    dire, cnt = map(int, input().split())
    visited = [[False] * n for _ in range(n)]
    for i in range(len(cloud)):
        x, y = cloud[i][0] + cnt * direction[dire][0], cloud[i][1] + cnt * direction[dire][1]
        
        while x >= n:
            x -= n
        while x < 0:
            x += n
        while y >= n:
            y -= n
        while y < 0:
            y += n
            
        visited[x][y] = True
        maps[x][y] += 1
        cloud[i] = [x, y]
    
    cnt_add_cloud = []
    for x, y in cloud:
        cnt = 0
        for dx, dy in cloud_dir:
            nx, ny = x + dx, y + dy
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            if maps[nx][ny] > 0:
                cnt += 1
        cnt_add_cloud.append(cnt)
    
    for clo, cnt in zip(cloud, cnt_add_cloud):
        maps[clo[0]][clo[1]] += cnt
    
    cloud = get_cloud(cloud)

ans = 0
for ma in maps:
    ans += sum(ma)
print(ans)
'''

from collections import deque
n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

direction = [[], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
cloud_dir = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
cloud = [[n - 1, 0], [n - 1, 1], [n - 2, 0], [n - 2, 1]]
cloud = deque(cloud)

def get_cloud():
    for i in range(n):
        for j in range(n):
            if maps[i][j] > 1 and not visited[i][j]:
                cloud.append([i, j])
                maps[i][j] -= 2

def move_cloud(dire, cnt):
    global n
    len_cloud = len(cloud)

    for _ in range(len_cloud):
        x, y = cloud.popleft()
        dx, dy = direction[dire][0] * cnt, direction[dire][1] * cnt
        nx = (x + dx) % n
        ny = (y + dy) % n

        if nx < 0:
            nx += n
        if ny < 0:
            ny += n
        
        cloud.append([nx, ny])
        visited[nx][ny] = True
        maps[nx][ny] += 1

def add_cloud():
    while cloud:
        x, y = cloud.popleft()
        for dx, dy in cloud_dir:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if maps[nx][ny] > 0:
                    maps[x][y] += 1
         
for _ in range(m):
    dire, cnt = map(int, input().split())
    visited = [[False] * n for _ in range(n)]

    move_cloud(dire, cnt)

    add_cloud()
    
    get_cloud()

ans = 0
for ma in maps:
    ans += sum(ma)
print(ans)
