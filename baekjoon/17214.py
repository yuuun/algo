## https://velog.io/@delicate1290/백준-문제-풀이-다항-함수의-적분-17214번
'''
최대 1차항!!!
1) -?\d+x : -로 시작하는 값을 받을 수 있음
2) [-, +]?\d+$: 상수항이 마지막으로 끝남
'''

import re
poly = input()
if poly == '0':
    print('W')
    exit()

res = ''
first_term = re.findall('-?\d+x', poly)
constant = re.findall('[-, +]?\d+$', poly)

if first_term:
    n = str(int(first_term[0][:-1]) // 2)
    if n[0].isdigit() or n[0] == '+':
        sign = ''
    else:
        sign = '-'
    
    if n in ['1', '-1']:
        res += sign + 'xx'
    else:
        res += n + 'xx'

if constant:
    n = constant[0]
    if n not in ['+0', '-0']:
        if n[0].isdigit() or n[0] == '+':
            sign = '+'
        else:
            sign = '-'
        if n == '1':
            res += 'x'
        elif n in ['+1', '-1']:
            res += sign + 'x'
        else:
            res += n + 'x'

res += '+W'

print(res)