## 삼성 코테 - 30분
r, c, t = map(int, input().split())
maps = []
air_condition = [] # 공기 청정기 위치 (항상 1행에 존재)

for i in range(r):
    tmp = list(map(int, input().split()))
    maps.append(tmp)
    for tm in tmp:
        if tm == -1:
            air_condition.append(i)

dxy = [[1, 0], [-1, 0], [0, -1], [0, 1]]
def checkCriteria(i, j):
    if 0 <= i < r and 0 <= j < c:
        return True
    return False

def spread_dust():
    added_maps = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            spreaded = maps[x][y] // 5
						# 값이 0이상인 칸만 계산하여 미세먼지를 퍼트림
            if spreaded > 0:
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if checkCriteria(nx, ny) and maps[nx][ny] != -1:
                        added_maps[x][y] -= spreaded
                        added_maps[nx][ny] += spreaded
    
    # add dust
    for x in range(r):
        for y in range(c):
            maps[x][y] += added_maps[x][y]


def move_air():
    # 공기청정기의 윗부분
    # 1) 아래로 내려오기
    a1, a2 = air_condition[0], air_condition[1]
    for i in range(a1 - 1, 0, -1):
        maps[i][0] = maps[i - 1][0]
    
    # 2) 왼쪽으로 이동하기
    for j in range(c - 1):
        maps[0][j] = maps[0][j + 1]

    # 3) 위로 이동하기
    for i in range(a1):
        maps[i][-1] = maps[i + 1][-1]

    # 4) 오른쪽으로 이동하기
    for j in range(c - 1, 1, -1):
        maps[a1][j] = maps[a1][j - 1]
    maps[a1][1] = 0   #공기청정기 바로 오른쪽에 있는 경우 제외시켜주어야 함
        
    # 공기청정기 아랫부분
    # 1) 위로 올라오기
    for i in range(a2 + 1, r - 1):
        maps[i][0] = maps[i + 1][0]
    
    # 2) 왼쪽 이동하기
    for j in range(c - 1):
        maps[-1][j] = maps[-1][j + 1]
    
    # 3) 아래로 이동하기
    for i in range(r - 1, a2, -1):
        maps[i][-1] = maps[i - 1][-1]
    
    # 4) 오른쪽 이동하기
    for j in range(c - 1, 1, -1):
        maps[a2][j] = maps[a2][j - 1]
    maps[a2][1] = 0   #공기청정기 바로 오른쪽에 있는 경우 제외시켜주어야 함

def cnt_dust():
    cnt = 2
    for i in range(r):
        cnt += sum(maps[i])
    return cnt

# t회 반복
for _ in range(t):
    spread_dust()
    move_air()

print(cnt_dust())