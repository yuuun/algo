#시간초과
n, a = int(input()), sorted(list(map(int, input().split())))
m, b = int(input()), list(map(int, input().split()))

def binary_search(bb, start, end):
    if start > end:
        return 0
    m = (start + end) // 2
    if bb == a[m]:
        return 1
    elif bb < a[m]:
        return binary_search(bb, start, m - 1)
    else:
        return binary_search(bb, m + 1, end)

ans = []
for bb in b:
    tmp = binary_search(bb, 0, n - 1)
    if tmp == 0:
        ans.append(tmp)
    else:
        ans.append(a.count(bb))
print(' '.join(map(str, ans)))