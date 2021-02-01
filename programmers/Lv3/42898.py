def solution(m, n, puddles):
    answer = move(1, 1, puddles, (m + 1), (n + 1))
    return answer

def move(x, y, puddles, m, n):
    visited = [[0 for i in range(n)] for j in range(m)]
    for i in range(1, n):
        if [1, i] in puddles:
            break
        visited[1][i] = 1
    for j in range(1, m):
        if [j, 1] in puddles:
            break
        visited[j][1] = 1

    for i in range(x + 1,  m):
        for j in range(y + 1, n):
            if [i, j] not in puddles:
                visited[i][j] = visited[i - 1][j] + visited[i][j - 1]

    return visited[m - 1][n - 1] % 1000000007

print(solution(4, 3, [[2, 2]]))