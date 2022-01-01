import sys
n = int(input())
origin = input()

nums, ops = [], []
for e in origin:
    if e.isdigit():
        nums.append(e)
    else:
        ops.append(e)

def sol(idx, tot):
    global answer
    if idx == len(ops):
        answer = max(answer, int(tot))
        return
    
    cal = str(eval(tot + ops[idx] + nums[idx + 1]))
    sol(idx + 1, cal)

    if idx + 1 < len(ops):
        cal = str(eval(nums[idx + 1] + ops[idx + 1] + nums[idx + 2]))
        cal = str(eval(tot + ops[idx] + cal))
        sol(idx + 2, cal)
answer = -sys.maxsize
sol(0, nums[0])
print(answer)