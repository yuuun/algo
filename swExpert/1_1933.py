import math
val = int(input())
sqrt_val = math.ceil(math.sqrt(val))
ans_list = list()
for i in range(1, sqrt_val + 1):
    if val % i == 0:
        ans_list.append(i)
        ans_list.append(int(val / i))
print(" ".join(str(i) for i in sorted(ans_list)))