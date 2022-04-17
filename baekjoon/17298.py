n = int(input())
arr = list(map(int, input().split()))
ans = []
stack = []

for i in range(n - 1, -1, -1):
    while stack:
        if arr[i] < stack[-1]:
            ans.append(stack[-1])
            break
        else:
            stack.pop()

    if not stack:
        ans.append(-1)
    stack.append(arr[i])
print(' '.join(map(str, ans[::-1])))