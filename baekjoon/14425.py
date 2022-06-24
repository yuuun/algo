n, m = map(int, input().split())
s = set()
for _ in range(n):
    s.add(input())

ans = 0
for _ in range(m):
    if input() in s:
        ans += 1

print(ans)