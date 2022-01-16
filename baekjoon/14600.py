k = int(input())
n = 2 ** k
x, y = map(int, input().split())
x, y = x - 1, n - y

maps = [[0] * n for _ in range(n)]
maps[x][y] = -1

def fill(x, y):
    global num, n
    num += 1
    pos = [[x + n - 1, y + n - 1], [x + n, y + n - 1], 
            [x + n - 1, y + n], [x + n, y + n]]


num = 0
fill(0, 0)
