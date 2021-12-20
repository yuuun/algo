# https://www.acmicpc.net/problem/9342
import re
checkAlpha = re.compile('[A-F]{0,1}A+F+C+[A-F]{0,1}')
ans = ''
for t in range(int(input())):
    cand = input()
    m = checkAlpha.match(cand)
    # 문자열 안에 checkAlpha에 해당하는 문자열이 포함하기만 하면 무조건 값을 반환해주기 때문에 길이도 맞는지 체크를 해줘야됨
    if m is None:
        print("Good")
    else:   
        s, e = m.start(), m.end()
        if e - s == len(cand):
            print('Infected!')
        else:
            print("Good")