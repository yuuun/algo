nums = list(map(int, input().split()))

ans = [i for i in range(1, len(nums) + 1)]

while nums != ans:
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            print(' '.join(map(str, nums)))