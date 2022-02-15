### 시간 초과
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
            if maps[i][j] > 1 and [i, j] not in cloud:
                new_cloud.append([i, j])
                maps[i][j] -= 2
    return new_cloud

direction = [[], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
cloud_dir = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
for _ in range(m):
    dire, cnt = map(int, input().split())
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
