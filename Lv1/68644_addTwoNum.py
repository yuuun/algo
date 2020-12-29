def solution(numbers):
    answer = []
    for idx1, num1 in enumerate(numbers):
        for num2 in numbers[idx1+1:]:
            num3 = num1 + num2
            #여기서 return할 때, set(answer)으로 설정할 경우, 중복값을 제거해줌
            if num3 not in answer:
                answer.append(num1 + num2)
    answer.sort()
    return answer

print(solution([2,1,3,4,1]))