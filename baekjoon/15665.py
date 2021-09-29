n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

ans = []
def solve(depth):
    if depth == m:
        print(' '.join(map(str, ans)))
        return
    tmp = 0
    for i in range(n):
        if tmp != nums[i]:
            ans.append(nums[i])
            tmp = nums[i]
            solve(depth + 1)
            ans.pop()
solve(0)