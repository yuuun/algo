brac = input()
stack = []
answer = 0
tmp = 1

for i, t in enumerate(brac):
    if t == '(':
        stack.append(t)
        tmp *= 2
    elif t == '[':
        stack.append(t)
        tmp *= 3
    elif t == ')':
        if not stack or stack[-1] == '[':
            print(0)
            exit()
        if brac[i - 1] == '(':
            answer += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            print(0)
            exit()
        if brac[i - 1] == '[':
            answer += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)