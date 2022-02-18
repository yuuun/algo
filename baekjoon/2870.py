import re
n  = int(input())
nums = []
for _ in range(n):
    for t in re.split('\\D', input()): 
            #   re.split('\\D', '1103dkfslklj212kfj3')
            #   ['1103', '', '', '', '', '', '', '', '212', '', '', '3']
        if t != '':
            nums.append(int(t))
nums = sorted(nums)
print('\n'.join(map(str, nums)))