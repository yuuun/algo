import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
k = int(input())
visited = [False] * n

def delete_node(idx):
    nums[idx] = -2
    for i in range(n):
        if nums[i] == idx and not visited[i]:
            visited[i] = True
            delete_node(i)

delete_node(k)
cnt = 0
for i in range(n):
    if nums[i] != -2 and i not in nums:
        cnt += 1

print(cnt)