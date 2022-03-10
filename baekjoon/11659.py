n, m = map(int, input().split())
nums = list(map(int, input().split()))

for i, j in zip(range(1, n), range(n)):
    nums[i] += nums[j]
nums = [0] + nums
for _ in range(m):
    i, j = map(int, input().split())
    print(nums[j] - nums[i - 1])