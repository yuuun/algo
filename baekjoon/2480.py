from collections import defaultdict
arr = sorted(list(map(int, input().split())))
dic = defaultdict(int)
for a in arr:
    dic[a] += 1

ans = 0
tmp = 0
for i, v in dic.items():
    if v == 3:
        ans += 10000 + i * 1000
        break
    elif v == 2:
        ans += 1000 + i * 100
        break
    else:
        tmp = i
if ans != 0:
    print(ans)
else:
    print(tmp * 100)