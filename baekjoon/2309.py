from itertools import combinations
arr = sorted([int(input()) for _ in range(9)], reverse=True)
sum_arr = sum(arr) - 100

for a, b in combinations(arr, 2):
    if a + b == sum_arr:
        arr.remove(a)
        arr.remove(b)
        break
for a in arr[::-1]:
    print(a)