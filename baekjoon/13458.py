import math
n = int(input())
a_list = list(map(int, input().split()))
b, c = map(int, input().split())

ans = 0
for a in a_list:
    ans += 1
    a -= b
    if a > 0:
        ans += math.ceil(a / c)
print(ans)