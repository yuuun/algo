n = int(input())
arr = sorted(list(map(int, input().split())))
brr = sorted(list(map(int, input().split())), reverse=True)
ans = 0
for a, b in zip(arr, brr):
    ans += a * b
print(ans)