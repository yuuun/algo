from collections import deque
n = int(input())

dxy = [[0, 2], [1, 1], [1, -1], [0, -2], [-1, -1], [-1, 1]]
dic = {0:[1, 5], 1:[0, 2], 2:[1, 3], 3:[2, 4], 4:[3, 5], 5:[4, 0]}

visited = [[False] * 100 for _ in range(100)]
ans = 0
def dfs(x, y, cnt, d):
    global ans
    if cnt == n:
        if visited[x][y]:
            ans += 1
        return
    
    if visited[x][y]:
        return
    
    visited[x][y] = True
    cnt += 1
    for i in dic[d]:
        dx, dy = dxy[i]
        dfs(x + dx, y + dy, cnt, i)
    visited[x][y] = False

visited[50][50] = True
dfs(50, 52, 0, 0)
print(ans)


'''
print([0,0,0,0,0,2,2,4,8,26,36,80,148,332,556,1172,2112,4350,7732,15568,28204,56100,101640][int(input())])

'''