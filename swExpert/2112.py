def check(maps):
    for j in range(w):
        cnt = 1
        for i in range(d - 1):
            if cnt == k:
                break
            elif maps[i][j] == maps[i + 1][j]:
                cnt += 1
            else:
                cnt = 1
        if cnt != k:
            return False
    return True
    
def dfs(idx, depth, maps):
    global ans
    if depth > ans:
        return
    
    if check(maps):
        ans = depth
        return
    
    if idx == d:
        return
    dfs(idx + 1, depth, maps)
    dfs(idx + 1, depth + 1, maps[:idx] + [[0] * w] + maps[idx + 1:])
    dfs(idx + 1, depth + 1, maps[:idx] + [[1] * w] + maps[idx + 1:])

for z in range(1, int(input()) + 1):
    d, w, k = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(d)]
    ans = d
    dfs(0, 0, maps)

    print('#{0} {1}'.format(z, ans))