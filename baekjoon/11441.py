import sys
input = sys.stdin.readline
n = int(input())
a = [0] + list(map(int, input().split()))

for i, j in zip(range(1, n), range(2, n + 1)):
    a[j] += a[i]

for _ in range(int(input())):
    i, j = map(int, input().split())
    print(a[j] - a[i - 1])