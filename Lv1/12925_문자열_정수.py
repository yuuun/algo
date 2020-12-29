def solution(s):
    return -int(s[1:]) if s[0] == '-' else int(s)
print(solution("-1234"))