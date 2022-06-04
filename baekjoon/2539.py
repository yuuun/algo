n, m = map(int, input().split())
k = int(input())
arr = [[True] * m for _ in range(n)]
for _ in range(int(input())):
    x, y = map(lambda x: int(x) - 1, input().split())
    arr[x][y] = False
print(arr)