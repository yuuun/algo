n = int(input())
tops = list(map(int, input().split()))
stack, answer = [], []
for i in range(n):
    while stack:
        if stack[-1][1] > tops[i]:
            answer.append(stack[-1][0])
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i + 1, tops[i]])
print(' '.join(map(str, answer)))

# n = int(input())
# tops = list(map(int, input().split()))
# 
# answer = []
# for i in range(n - 1, 0, -1):
#     flag = True
#     for j in range(i - 1, -1, -1):
#         if tops[i] <= tops[j]:
#             answer.append(j + 1)
#             flag = False
#             break
#     if flag:
#         answer.append(0)
# answer.append(0)
# print(' '.join(map(str, answer[::-1])))