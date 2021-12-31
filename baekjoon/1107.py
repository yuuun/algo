#TBD
n = int(input())
m = int(input())
print(list(map(int, input().split())))
import pdb; pdb.set_trace()
but = [i for i in range(10)].remove(list(map(int, input().split())))

min_cnt = abs(n - 100)

for nu in range(1000001):
    num = str(nu)
    for i in range(len(num)):
        if num[i] not in but:
            break
        elif i == len(num) - 1:
            min_cnt = min(min_cnt, len(num) + abs(n - nu))
print(min_cnt)