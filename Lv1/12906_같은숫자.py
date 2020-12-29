def solution(arr):
    answer = [arr[0]]
    for val in arr[1:]:
        if val != answer[-1]:
             answer.append(val)
    return answer
print(solution([1,1,3,3,0,1,1]))