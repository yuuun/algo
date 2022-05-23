import math
n = int(input())
n_chicken = 0
for k in input():
    if k == 'C':
        n_chicken += 1
n = n - n_chicken + 1
print(math.ceil(n_chicken / n))