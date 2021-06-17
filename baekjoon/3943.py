#구현 - 시간 초과 수정해야됨
n = int(input())

def hail(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return 3 * n + 1

for _ in range(n):
    k = int(input())
    if k in [4, 2, 1]:
        print(k)
    else:
        max_k = k
        while k not in [4, 2, 1]:
            k = hail(k)
            if max_k < k:
                max_k = k
        print(max_k)