test_case = int(input())
nums = list(map(int, input().split()))

ans = [1 for _ in range(test_case)]
for idx in range(1, test_case):
    for i in range(idx):
        if nums[idx] > nums[i]:
            ans[idx] = max(ans[idx], ans[i] + 1)
print(max(ans))