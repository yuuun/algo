n, m, x, y, k = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

directions = list(map(int, input().split()))

dxy = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]    # 동, 서, 북, 남
dice = [0, 0, 0, 0, 0, 0, 0] # idx를 위해서 앞에 허수 붙여줌 

def change_dice(t):
    if t == 1: # 동 - 2, 5 그대로
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif t == 2: # 서 - 2, 5 그대로
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif t == 3: # 북 - 3, 4 그대로
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    else: # 남 - 3, 4 그대로
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

for t in directions:
    dx, dy = dxy[t][0], dxy[t][1]
    nx, ny = x + dx, y + dy
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    change_dice(t)
    if maps[nx][ny] == 0:
        maps[nx][ny] = dice[6]
    else:
        dice[6] = maps[nx][ny]
        maps[nx][ny] = 0
    x, y = nx, ny
    print(dice[1])