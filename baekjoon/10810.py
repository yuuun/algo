n, m = map(int, input().split())
ball = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b, num = map(int, input().split())
    for i in range(a, b + 1):
        ball[i] = num
print(' '.join(map(str, ball[1:])))