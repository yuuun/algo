def solution(s):
    if len(s) == 4 or len(s) == 6:
        for ss in s:
            if '0' > ss or ss > '9':
                return False
        return True
    else:
        return False
print(solution("a213"))
print(solution("1234"))