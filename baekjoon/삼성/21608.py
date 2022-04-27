from collections import deque
n = int(input())
student = {}
for _ in range(n ** 2):
    tmp = list(map(int, input().split()))
    student[tmp[0]] = tmp[1:]

dxy = [[0, 1], [1, 0], [-1, 0], [0, -1]]
maps = [[0] * n for _ in range(n)]
for k, v in student.items():
    max_x, max_y = 0, 0
    max_like = -1
    max_empty = -1
    
    for x in range(n):
        for y in range(n):
            if maps[x][y] == 0:
                cnt_empty = 0
                cnt_like = 0
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n:
                        if maps[nx][ny] == 0:
                            cnt_empty += 1
                        elif maps[nx][ny] in v:
                            cnt_like += 1
                
                if cnt_like > max_like or (cnt_like == max_like and cnt_empty > max_empty):
                    max_x, max_y = x, y
                    max_like, max_empty = cnt_like, cnt_empty
    
    maps[max_x][max_y] = k

ans = 0
dict = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
for x in range(n):
    for y in range(n):
        cnt = 0
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] in student[maps[x][y]]:
                cnt += 1
        ans += dict[cnt]
print(ans)