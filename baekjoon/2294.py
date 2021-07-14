n, k = map(int, input().split())
c = [int(input()) for _ in range(n)]
cnt = 0

for i in c[::-1]:
    while True:
        tmp = k // i
        print(k, i, tmp)
        if tmp > 0:
            k -= i
            cnt += 1
        else:
            break
print(cnt)