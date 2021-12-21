n = int(input())
paths = []

for i in range(n - 1):
    tmp = list(map(int, input().split()))
    for j in tmp[i + 1:]:
        