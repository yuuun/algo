#dp
inp = int(input())
candidate = [0] * (inp + 1)

for i in range(2, inp + 1):
    candidate[i] = candidate[i - 1] + 1
    if i % 2 == 0:
        tmp = i // 2
        if candidate[i] > candidate[tmp] + 1:
            candidate[i] = candidate[tmp] + 1
    if i % 3 == 0:
        tmp = i // 3
        if candidate[i] > candidate[tmp] + 1:
            candidate[i] = candidate[tmp] + 1

print(candidate[inp])