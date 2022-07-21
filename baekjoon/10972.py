n = int(input())
m = list(map(int, input().split()))
find = False
for i in range(n - 1, 0, -1):
    if m[i - 1] < m[i]:
        for j in range(n - 1, 0, -1):
            if m[i - 1] < m[j]:
                m[i - 1], m[j] = m[j], m[i - 1]
                m = m[:i] + sorted(m[i:])
                find = True
                break
    if find:
        print(' '.join(map(str, m)))
        break
if not find:
    print(-1)