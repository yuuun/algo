import sys
input = sys.stdin.readline
n, q = map(int, input().split())
a = [0] + sorted(list(map(int, input().split())))

for i, j in zip(range(1, n), range(2, n + 1)):
    a[j] += a[i]

for _ in range(q):
    i, j = map(int, input().split())
    print(a[j] - a[i - 1])