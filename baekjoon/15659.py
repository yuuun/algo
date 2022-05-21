n = int(input())
nums = list(map(int, input().split()))
arr = list(map(int, input().split()))
dic = {0: '+', 1: '-', 2: '*', 3: '//'}
candidate = []

def sol(idx, string):
    global candidate
    if idx == n - 1:
        candidate.append(eval(string))
    for i in range(4):
        if arr[i] > 0:
            arr[i] -= 1
            sol(idx + 1, string + dic[i] + str(nums[idx + 1]))
            arr[i] += 1

sol(0, str(nums[0]))
candidate.sort()
print(candidate[-1])
print(candidate[0])