from collections import deque
n, m, k = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dice = [0, 1, 2, 3, 4, 5, 6]    # 첫번째 idx는 허수
sx, sy = 0, 0

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]] #동, 남, 서, 북으로 이동

def rotate_dice():
    global direction
    if direction == 0:      # 2, 5 고정
        dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]
    elif direction == 1:    # 3, 4 고정
        dice[1], dice[5], dice[6], dice[2] = dice[2], dice[1], dice[5], dice[6]
    elif direction == 2:    # 2, 5고정
        dice[1], dice[4], dice[6], dice[3] = dice[3], dice[1], dice[4], dice[6]
    elif direction == 3:    # 3, 4 고정
        dice[1], dice[2], dice[6], dice[5] = dice[5], dice[1], dice[2], dice[6]

def decide_direction(dice_num, map_num):
    global direction
    if dice_num > map_num:
        direction = (direction + 1) % 4
    elif dice_num < map_num:
        direction = (direction + 3) % 4
        
def is_map(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

score = [[0] * m for _ in range(n)]

def calculate_score():
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                q = deque()
                q.append([i, j])
                visited[i][j] = True
                cnt, sc = 1, maps[i][j]
                candidate = [[i, j]]
                while q:
                    x, y = q.popleft()
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        if is_map(nx, ny) and maps[nx][ny] == sc and not visited[nx][ny]:
                            q.append([nx, ny])
                            visited[nx][ny] = True
                            candidate.append([nx, ny])
                            cnt += 1
                
                for x, y in candidate:
                    score[x][y] = cnt  * sc

calculate_score()

tot = 0
direction = 0

for i in range(k):
    nx = sx + dxy[direction][0]
    ny = sy + dxy[direction][1]
    if not is_map(nx, ny):
        direction = (direction + 2) % 4
        nx = sx + dxy[direction][0]
        ny = sy + dxy[direction][1]

    tot += score[nx][ny]
    rotate_dice()
    decide_direction(dice[6], maps[nx][ny])
    sx, sy = nx, ny

print(tot)