# 시간 초과
n, m = map(int, input().split())

table = [[0] * (n + 1)]
for _ in range(n):
    table.append([0] + list(map(int, input().split())))

for r in range(1, n + 1):
    for c in range(1, n + 1):
        table[r][c] += table[r][c - 1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ans = 0
    for k in range(x1, x2 + 1):
        if y1 != 0:
            ans -= table[k][y1 - 1]
        ans += table[k][y2]
        
    print(ans)
