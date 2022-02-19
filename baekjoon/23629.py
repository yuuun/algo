string = input()

s = string.replace('ZERO', '0')
s = s.replace('ONE', '1')
s = s.replace('TWO', '2')
s = s.replace('THREE', '3')
s = s.replace('FOUR', '4')
s = s.replace('FIVE', '5')
s = s.replace('SIX', '6')
s = s.replace('SEVEN', '7')
s = s.replace('EIGHT', '8')
s = s.replace('NINE', '9')

def find_sign():
    sign_idx = [-1]
    sign = []
    for i, st in enumerate(s[:-1]):
        if st == '=':
            return False, False
        if st in ['+', '-', 'x', '/']:
            # 연산자가 두개 연속으로 있을 경우, Madness 출력
            if i - sign_idx[-1] == 1: 
                return False, False
            else:
                sign_idx.append(i)
                sign.append(st)
    return sign_idx[1:], sign

def change_num(num):
    num = num.replace('0', 'ZERO')
    num = num.replace('1', 'ONE')
    num = num.replace('2', 'TWO')
    num = num.replace('3', 'THREE')
    num = num.replace('4', 'FOUR')
    num = num.replace('5', 'FIVE')
    num = num.replace('6', 'SIX')
    num = num.replace('7', 'SEVEN')
    num = num.replace('8', 'EIGHT')
    num = num.replace('9', 'NINE')

    return num

sign_idx, sign = find_sign()

if sign_idx == []:   # 식에 연산자가 없을 경우 자기 자신 그대로 출력
    print(s)
    print(string[:-1])
elif sign_idx:
    import re
    num = [int(i) for i in re.split('\\D', s) if i != '']
    if len(num) != len(sign) + 1:
        print('Madness!')
        exit()
    ans = num[0]
    for n, si in zip(num[1:], sign):
        if si == 'x':
            ans *= n
        elif si == '+':
            ans += n
        elif si == '-':
            ans -= n
        elif si == '/':
            ans /= n
            ans = int(ans)
    print(s)
    print(change_num(str(ans)))

else:
    print('Madness!')