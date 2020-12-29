def solution(arr, divisor):
    answer = list(a for a in arr if a % divisor == 0)
    if answer == []:
        answer = [-1]
    else:
        answer.sort()
    return answer
print(solution([5, 7, 9, 10], 5))