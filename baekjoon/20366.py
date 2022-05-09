n = int(input())
arr = sorted(list(map(int, input().split())))

ans = 1e20

for i in range(n):
    for j in range(i + 3, n):
        l, r = i + 1, j - 1
        while l < r:
            t = (arr[i] + arr[j]) - (arr[l] + arr[r])
            if ans > abs(t):
                ans = abs(t)
            if t < 0:
                r -= 1
            else:
                l += 1
print(ans)
