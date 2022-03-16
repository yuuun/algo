n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
cnt = [0] * (n + 2)
for _ in range(m):
    i, j, k = map(int, input().split())
    cnt[i] += k
    cnt[j + 1] -= k
    
for i, j in zip(range(1, n + 2), range(n + 2)):
    cnt[i] += cnt[j]

for i in range(1, n + 1):
    a[i] += cnt[i]
print(' '.join(map(str, a[1:])))