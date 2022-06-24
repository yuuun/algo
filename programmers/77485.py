def solution(rows, columns, queries):
    maps = []
    t = 1
    for _ in range(rows):
        tmp = []
        for _ in range(columns):
            tmp.append(t)
            t += 1
        maps.append(tmp)

    answer = []
    for x, y, a, b in queries:
        x, y = x - 1, y - 1
        a, b = a - 1, b - 1
        t = maps[x][y]
        min_val = t
        for i in range(x, a):
            maps[i][y] = maps[i + 1][y]
            min_val = min(min_val, maps[i][y])
        for j in range(y, b):
            maps[a][j] = maps[a][j + 1]
            min_val = min(min_val, maps[a][j])
        for i in range(a, x, -1):
            maps[i][b] = maps[i - 1][b]
            min_val = min(min_val, maps[i][b])
        for j in range(b, y, -1):
            maps[x][j] = maps[x][j - 1]
            min_val = min(min_val, maps[x][j])
        maps[x][y + 1] = t
        answer.append(min_val)
    return answer

print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]), [8, 10, 25])
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]), [1, 1, 5, 3])