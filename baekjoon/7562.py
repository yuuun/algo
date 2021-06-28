n = int(input())
d = [[2, -1], [2, 1], [-2, -1], [-2, 1],
    [1, 2], [1, -2], [-1, 2], [-1, -2]]
for _ in range(n):
    k = int(input())
    x, y = map(int, input().split())
    desx, desy = map(int, input().split())
    