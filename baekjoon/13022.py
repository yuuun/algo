string = input()

def check(s):
    cnt = 0
    while s[cnt] == 'w':
        cnt += 1
    len_cnt = 4 * cnt
    if s[:len_cnt] == 'w' * cnt + 'o' * cnt + 'l' * cnt + 'f' * cnt:
        return True, len_cnt
    return False, 0

i = 0
while i < len(string):
    if string[i] == 'w':
        isTrue, t = check(string[i:])
        if not isTrue:
            print('0')
            exit()

        i += t
        
    else:
        print('0')
        exit()
print('1')