n = int(input())
m = int(input())

nums = sorted([int(input()) for _ in range(m)])
if 1 not in nums:
    nums = [0] + nums
if n not in nums:
    nums = nums + [n + 1]

ans = []
for i in range(1, len(nums)):
    ans.append(nums[i] - nums[i - 1] - 1)

max_val = max(ans)
dp = [1, 1, 2]
for _ in range(max_val - 2):
    dp.append(dp[-1] + dp[-2])
    
tmp = 1
for a in ans:
    tmp *= dp[a]
print(tmp)