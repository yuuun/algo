n = int(input())
cust = [list(map(str, input().split())) for _ in range(n)]

cust = sorted(cust, key=lambda x: int(x[0]))
for cus in cust:
    print(' '.join(cus))