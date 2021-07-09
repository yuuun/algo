n = int(input())
cnt = 0
while True:
    if n % 5 == 0:
        print(n // 5 + cnt)
        break
    elif n < 0:
        print(-1)
        break
    n -= 3
    cnt += 1