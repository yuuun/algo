from collections import deque

n, m, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

tx, ty = map(int, input().split())
tx -= 1
ty -= 1

start = []
end = []
for i in range(m):
    sx, sy, ex, ey = map(int, input().split())
    start.append([sx - 1, sy - 1])
    end.append([ex - 1, ey - 1])
customer = [False] * m

def is_criteria(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

# 시작 지점에서 각 지점까지의 거리 반환
def calculate_dist(x, y):
    dist_map = [[0] * n for _ in range(n)]
    q = deque()
    q.append([x, y, 1])
    visited = [[False] * n for _ in range(n)]
    while q:
        x, y, c = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if is_criteria(nx, ny) and not visited[nx][ny]:
                if maps[nx][ny] == 0:   # 갈 수 없는 경우를 제외시켜줄 것
                    visited[nx][ny] = True
                    dist_map[nx][ny] = c
                    q.append([nx, ny, c + 1])
    return dist_map

def find_customer():
    global k
    tmp = []    #택시와 고객 사이의 거리를 계산하기 위한 변수
    dist_map = calculate_dist(tx, ty)
    for i in range(m):
        if not customer[i]:
            sx, sy = start[i][0], start[i][1]
            if sx == tx and sy == ty:       # 택시의 현 위치가 고객의 위치와 동일할 수 있음
                tmp.append([0, sx, sy, i])
            else:
                dist = dist_map[sx][sy]
                if dist != 0 and k >= dist: # 거리가 0일 경우에는, 택시가 고객이 있는 곳으로 이동 불가
                    tmp.append([dist, sx, sy, i])
    
    # 아무것도 tmp에 들어가지 않을 경우, 불가능
    if not tmp:
        return -1
    
    # 거리, 행, 열 순으로 정렬
    dist, _, _, idx = sorted(tmp)[0]
    k -= dist
    customer[idx] = True
    return idx

# 고객의 시작점에서 도착점까지 걸리는 시간 확인
def go_dst(sx, sy, ex, ey):
    global k, tx, ty
    dist = calculate_dist(sx, sy)[ex][ey]
    # 도착 거리가 0일 경우, 이동이 불가능
    if dist == 0:
        return False
    if k >= dist:
        k += dist
        tx, ty = ex, ey
        return True
    
    else:
        return False

num_cust = 0
while num_cust < m:
    cust_idx = find_customer()
    if cust_idx == -1:
        print(-1)
        exit()
    if go_dst(start[cust_idx][0], start[cust_idx][1], end[cust_idx][0], end[cust_idx][1]):
        num_cust += 1
    else:
        print(-1)
        exit()
        
print(k)
    
