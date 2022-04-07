n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
horse = {}
move_dir = {0:1, 1:0, 2:3, 3:2}
dxy = [[0, 1], [0, -1], [-1, 0], [1, 0]]
maps = [[[] for _ in range(n)] for _ in range(n)] # 말, 방향

def move_horse(idx):
    x, y, d = horse[idx]
    nx, ny = x + dxy[d][0], y + dxy[d][1]
    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 2:
        tmp = []
        while maps[x][y]:
            m, nd = maps[x][y].pop(0)
            tmp.append([m, nd])
            horse[m] = [nx, ny, nd]
            if m == idx:
                break
        
        if board[nx][ny] == 1:
            tmp = tmp[::-1]

        maps[nx][ny] = tmp + maps[nx][ny]
        if len(maps[nx][ny]) >= 4:
            print(cnt)
            exit()
        
    else:
        new_dir = move_dir[d]
        horse[idx][2] = new_dir
        for kk in range(len(maps[x][y])):
            if idx == maps[x][y][kk][0]:
                break
        maps[x][y][kk][1] = new_dir

        nx, ny = x + dxy[new_dir][0], y + dxy[new_dir][1]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 2:
            tmp = []
            while maps[x][y]:
                m, nd = maps[x][y].pop(0)
                tmp.append([m, nd])
                horse[m] = [nx, ny, nd]
                if m == idx:
                    break
            
            if board[nx][ny] == 1:
                tmp = tmp[::-1]

            maps[nx][ny] = tmp + maps[nx][ny]
            if len(maps[nx][ny]) >= 4:
                print(cnt)
                exit()
        

for i in range(k):
    x, y, d = map(lambda x: int(x) - 1, input().split())
    horse[i] = [x, y, d]
    maps[x][y] = [[i, d]]

cnt = 0
while cnt < 1001:
    cnt += 1
    for i in range(k):
        move_horse(i)
    

if cnt == 1001:
    print(-1)