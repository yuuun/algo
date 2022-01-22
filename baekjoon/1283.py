n = int(input())
alpha = [' ']

for _  in range(n):
    string = input()
    if string[0].upper() not in alpha:
        alpha.append(string[0].upper())
        print('[{0}]{1}'.format(string[0], string[1:]))
    else:
        st = string.split(' ')
        isTrue = True
        for i, s in enumerate(st):
            if s[0].upper() not in alpha:
                alpha.append(s[0].upper())
                isTrue = False
                print('{0} [{1}]{2} {3}'.format(' '.join(map(str, st[:i])), s[0], s[1:], ' '.join(map(str, st[i+1:]))))
                break

        if isTrue:
            idx = 1
            for st in string:
                if st.upper() in alpha:
                    print(st, end='')
                    idx += 1
                else:
                    alpha.append(st.upper())
                    print('[{0}]{1}'.format(st, string[idx:]))
                    break