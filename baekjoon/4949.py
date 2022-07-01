while True:
    tmp = input()
    isflag = True
    if tmp == '.':
        break
    stack = []
    for t in tmp:
        if t == '(' or t == '[':
            stack.append(t)
        elif t == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                isflag = False
                break
        elif t == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                isflag = False
                break
    if stack == [] and isflag:
        print('yes')
    else:
        print('no')