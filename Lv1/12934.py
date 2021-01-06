import math 
def solution(n):
    sqrt_val = math.sqrt(n)
    if sqrt_val.is_integer():
        return int((sqrt_val + 1) ** 2)
    else:
        return -1
print(solution(121))