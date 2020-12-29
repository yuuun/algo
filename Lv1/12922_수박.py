def solution(n):
    answer = ""
    #arr = ['수', '박']
    odd = False
    for _ in range(n):
        if odd:
            answer += '박'
            odd = False
        else:
            answer += '수'
            odd = True
    return answer
print(solution(10))