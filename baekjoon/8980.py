n_vill, max_weight = map(int, input().split())
n = int(input())

inputs = []
for _ in range(n):
    inputs.append(list(map(int, input().split())))

inputs = sorted(inputs, key=lambda x:(x[1], x[0]))

vill = [max_weight] * (n_vill + 1)
total = 0
for start, end, weight in inputs:
    tmp = max_weight

    for i in range(start, end):
        tmp = min(tmp, vill[i])
    tmp = min(tmp, weight)
    
    for i in range(start, end):
        vill[i] -= tmp
    total += tmp
print(total)