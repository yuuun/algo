n = int(input())
nums = list(map(int, input().split()))

num_list = sorted(list(set(nums)))
num_dic = {}
cnt = 0
for num in num_list:
    num_dic[num] = cnt
    cnt += 1

ans = []
for num in nums:
    ans.append(num_dic[num])
print(' '.join(map(str, ans)))