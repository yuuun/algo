n, m, h = map(int, input().split()) # 세로 선의 개수, 이미 연결된 사다리 정보, 가로 줄의 개수
maps = [[0] * n for _ in range(h)]
for _ in range(m):
    i, j = map(int, input().split())
    maps[i - 1][j - 1] = 1

#각 row별 사다리 움직이기
def check_possible():
    for j in range(n):
        s = j
        for i in range(h):
            if maps[i][s]:
                s += 1
            elif s > 0 and maps[i][s - 1]:
                s -= 1
        if s != j:
            return False
    return True

#최초 1회 가능한지 확인
if check_possible():
    print(0)
    exit()

ans = 4
def dfs(x, y, depth):
    global ans
    # depth가 현 시점에서 가장 최소값보다 작을 경우에는 굳이 확인할 필요 없음
    if depth >= ans:
        return
    if check_possible():
        ans = min(depth, ans)
        return

    for i in range(x, h):
        k = y if i == x else 0
        for j in range(k, n - 1):
            if maps[i][j] == 1:
                j += 1
            else:
                maps[i][j] = 1
                dfs(i, j + 2, depth + 1) # 연달아 사다리를 고려할 필요가 없기 때문에 j + 2를 해서 시간 복잡도를 감소
                maps[i][j] = 0
            

dfs(0, 0, 0)
print(ans if ans < 4 else -1)