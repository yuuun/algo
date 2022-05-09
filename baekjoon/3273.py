import sys
input = sys.stdin.readline
n = int(input())
a = sorted(list(map(int, input().split())))
k = int(input())
f, e = 0, n - 1
cnt = 0
while f < e:
    if a[f] + a[e] == k:
        cnt += 1
        f += 1
        e -= 1
    elif a[f] + a[e] < k:
        f += 1
    else:
        e -= 1
print(cnt)