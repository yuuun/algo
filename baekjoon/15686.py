n, m = map(int, input().split())
def combination(arr, k):
    for i in range(len(arr)):
        if k == 1:
            yield [arr[i]]
        else:
            for j in combination(arr[i + 1:], k - 1):
                yield [arr[i]] + j

stores = []
home = []

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 2: # 치킨집일 때
            stores.append([i, j])
        elif tmp[j] == 1:
            home.append([i, j])

min_val = 1e10
for store in combination(stores, m):
    ans = 0
    for hx, hy in home:
        _min = 1e10
        for nx, ny in store:
            _min = min(_min, abs(hx - nx) + abs(hy - ny))
        ans += _min
    min_val = min(min_val, ans)
print(min_val)