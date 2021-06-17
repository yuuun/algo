'''
4           
24 2 3 29   
25 30 30 30
'''
n = int(input())
left = list(map(int, input().split()))
plan = list(map(int, input().split()))

total = []
for l, p in zip(left, plan):
    total.append([l, p])

total = sorted(total, key=lambda total: (total[1], total[0]))
print(total)
ans = 0
for idx, t in enumerate(total):
    l, p = t
    cnt = 0
    print(total)
    if l < p:
        cnt = ((p - l - 1) // 30) + 1
    for idx2 in range(n - idx):
        total[idx + idx2][0] -= p
        total[idx + idx2][1] -= p
    ans += cnt
print(ans)
'''
total = sorted(total)
print(total)
ans = 0
for idx, t in enumerate(total):
    l, p = t
    if l < p:
        cnt = ((p - l - 1) // 30) + 1
    else:
        cnt = 0
    for idx2 in range(n - idx):
        total[idx + idx2][0] += p
    print(l, p, cnt, total)
    ans += cnt
print(ans)
'''