R, C = map(int, input().split())
K = int(input())
visited = [[False for _ in range(C)] for _ in range(R)]
for _ in range(K):
    obs_x, obs_y = map(int, input().split())
    visited[obs_x][obs_y] = True

sr, sc = map(int, input().split())

direction = list(map(int, input().split()))
for idx in range(len(direction)):
    direction[idx] -= 1
    
mov = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def is_pos(x, y):
    global R, C
    return 0 <= y < C and 0 <= x < R

cur = 0
tmp = 1
    
while True:
    print(visited)
    visited[sr][sc] = True
    if tmp == 4:
        break
    tmp_r, tmp_c = sr + mov[direction[cur]][0], sc + mov[direction[cur]][1]
    # print(tmp_r, tmp_c, sr, sc, visited)
    if is_pos(tmp_r, tmp_c) and not visited[tmp_r][tmp_c]:
        sr, sc = tmp_r, tmp_c
        tmp = 0
    else:
        tmp += 1
        cur = (cur + 1) % 4

print(sr, sc)