def solution(numbers):
    answer = []
    for n in numbers:
        for j in range(n + 1, int(10e15)):
            tmp = n & j
            print(tmp)
    return answer

print(solution([2, 7]))