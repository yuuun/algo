n = int(input())
nums = list(map(int, input().split()))
res = [nums[0]]
for i, j in zip(range(1, n), range(n)):
    res.append(res[j] + nums[i])

ans = 0
for i in range(n):
    ans += nums[i] * (res[-1] - res[i])
print(ans)