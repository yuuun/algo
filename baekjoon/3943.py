#구현 - 시간 초과 수정해야됨
n = int(input())
for _ in range(n):
    tmp = []
    k = int(input())
    while True:
        if 1 in tmp:
            break
        tmp.append(k)
        if k % 2 == 0:
            k //= 2
        else:
            k = 3 * k + 1
    print(max(tmp))