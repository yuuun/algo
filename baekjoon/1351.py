from collections import defaultdict
n, p, q = map(int, input().split())
arr = defaultdict(int)
arr[0] = 1

def dp(i):
    if arr[i]:
        return arr[i]
    if i == 0:
        return 1
    arr[i] = dp(i // p) + dp(i // q)
    return arr[i]

print(dp(n))