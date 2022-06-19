import sys
sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
maps = []
for _ in range(n):
    maps.append(list(input()))

dic = {'U': [-1, 0], 'R': [0, 1], 'D': [1, 0], 'L': [0, -1]}
check = [[False] * m for _ in range(n)] 

def dfs(x, y):
    if 0 <= x < n and 0 <= y < m:
        if maps[x][y] == True:
            return True
        elif maps[x][y] == False: 
            return False
        
        if check[x][y]:
            return False
        else:
            check[x][y] = True
            dx, dy = dic[maps[x][y]]
            nx, ny = x + dx, y + dy
            t = dfs(nx, ny)
            maps[x][y] = True if t else False
            return t
    else:
        return True

cnt = 0
for x in range(n):
    for y in range(m):
        if dfs(x, y):
            cnt += 1

print(cnt)
'''
import sys

# 재귀깊이 해제
sys.setrecursionlimit(600000)

# go : 현재 위치가 (i, j)일 때 밖으로 나가는 경로의 일부라면 1, 아니면 0을 리턴하는 함수
def go(i, j):
    # Base case : 밖으로 나가는 경우
    if i < 0 or i > n - 1 or j < 0 or j > m - 1:
        return 1
    # Memoization
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = 0
    # 점화식
    dp[i][j] = max(dp[i][j], go(i + cache[arr[i][j]][0], j + cache[arr[i][j]][1]))
    return dp[i][j]

# 입력부
n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

# dp : 2차원 상태 공간 배열
dp = [[-1] * m for _ in range(n)]

# cache : 현재 위치가 가리키는 방향을 key, 그 때 가야할 칸 수를 value로 갖는 dictionary
cache = {'L' : (0, -1), 'R' : (0, 1), 'U' : (-1, 0), 'D' : (1, 0)}
ans = 0

for i in range(n):
    for j in range(m):
        # 아직 방문하지 않은 경우
        if dp[i][j] == -1:
            # 밖으로 갈 수 있다면 정답 증가
            if go(i, j) != 0:
                ans += 1
        # 방문했고 밖으로 나갈 수 있는 경우 정답 증가
        elif dp[i][j] == 1:
            ans += 1
            
# 정답 출력
print(ans)

'''