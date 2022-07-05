arr = input()
stack = []
length = 0
tmp = ''
for a in arr:
    if a.isdigit():
        length += 1
        tmp = a
    elif a == '(':
        stack.append([tmp, length - 1])
        length = 0
    else:
        multi, preL = stack.pop()
        length = (int(multi) * length) + preL

print(length)
