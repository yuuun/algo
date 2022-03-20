n, s = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

def dfs(idx, sum):
    global cnt
    if idx >= n:
        return
    sum += nums[idx]
    if sum == s:
        cnt += 1
    dfs(idx + 1, sum - nums[idx])
    dfs(idx + 1, sum)

dfs(0, 0)
print(cnt)