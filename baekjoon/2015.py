# 4 0
# 2 -2 2 -2

# 6 5
# 1 2 3 4 5 0
from collections import defaultdict
n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    arr[i] += arr[i - 1]

prefix = defaultdict(int)
for i in range(n):
    if arr[i] == k:
        ans += 1
    ans += prefix[arr[i] - k]
    prefix[arr[i]] += 1
    print(prefix)

print(ans)