n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs(x, y, visited):
    q = deque()
    q.append([x, y])
    s =  maps[x][y]
    rainbow = []
    blocks = [[x, y]]
    block_cnt, rainbow_cnt = 1, 0 #같은 개수가 있을 경우 rainbow의 개수가 많은 순으로 접근할 것
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    if  maps[nx][ny] == s:
                        visited[nx][ny] = True
                        q.append([nx, ny])
                        blocks.append([nx, ny])
                        block_cnt += 1

                    if  maps[nx][ny] == 0:
                        visited[nx][ny] = True
                        q.append([nx, ny])
                        rainbow.append([nx, ny])
                        blocks.append([nx, ny])
                        block_cnt += 1
                        rainbow_cnt += 1

    ## rainbow에 해당 할 경우 방문 기록 삭제
    for x, y in rainbow:
        visited[x][y] = False
    
    return block_cnt, rainbow_cnt, blocks, visited
            

def remove_block():
    visited = [[False] * n for _ in range(n)]
    candidate = []
    for i in range(n):
        for j in range(n):
            if  maps[i][j] > 0 and not visited[i][j]:
                visited[i][j] = True
                block_cnt, rainbow_cnt, blocks, visited = bfs(i, j, visited)
                if block_cnt > 1:
                    candidate.append([block_cnt, rainbow_cnt, blocks])     # 후보에 block score, block 개수, block list

    if len(candidate) == 0:
        return None, 0
    
    candidate = sorted(candidate, reverse=True)

    blocks = candidate[0][2]
    added_score = candidate[0][0] ** 2

    for x, y in blocks:
         maps[x][y] = -2
    
    return blocks, added_score

def gravity():
    for i in range(n - 2, -1, -1):
        for j in range(n):
            if maps[i][j] > -1:
                r = i
                while True:
                    if 0 <= r + 1 < n and maps[r + 1][j] == -2:
                        maps[r + 1][j] = maps[r][j]
                        maps[r][j] = -2
                        r += 1
                    else:
                        break

def rotate():
    global maps
    new_block = []
    for j in range(n - 1, -1, -1):
        tmp = []
        for i in range(n):
            tmp.append(maps[i][j])
        new_block.append(tmp)

    maps = new_block

score = 0
while True:
    blocks, added_score = remove_block()
    if blocks == None:
        break
    score += added_score
    gravity()
    rotate()
    gravity()

print(score)