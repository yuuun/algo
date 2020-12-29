def solution(seoul):
    for idx, se in enumerate(seoul):
        if se is 'Kim':
            return '김서방은 ' + str(idx)+ '에 있다'
    #return list(idx for idx, se in enumerate(seoul) if se is 'Kim')[0]
print(solution(["Jane", "Kim"]))