n = int(input())
num = list(map(int, input().split()))

ans = 0
for i in range(len(num)):
    for j in range(i + 1, len(num)):
        ans += num[i] * num[j]
print(ans)