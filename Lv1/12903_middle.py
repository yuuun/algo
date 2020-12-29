def solution(s):
    answer = ''
    loc = len(s) // 2
    if len(s) % 2 == 0:
        answer = s[loc - 1: loc + 1]
    else: 
        answer = s[loc : loc + 1]
    return answer
print(solution("abcde"))
print(solution("qwer"))
