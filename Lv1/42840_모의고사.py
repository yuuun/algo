def solution(answers):
    answer = []
    
    student = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    score = []
    
    for stu in student:
        src = 0
        for idx, ans in enumerate(answers):
            if ans == stu[idx % len(stu)]:
                src += 1
        score.append(src)
    
    #중복값일 경우에 추가시켜줘야되기 때문에 아래 단계 진행.
    max_value = max(score)
    answer = [idx + 1 for idx, j in enumerate(score) if j == max_value]
    answer
    
    return answer
print(solution([1,2,3,4,5]))
print(solution([1,3, 2,4,2]))