def solution(n):
    answer = list(int(val) for val in list(str(n)))
    answer.reverse()
    return answer

print(solution(12345))