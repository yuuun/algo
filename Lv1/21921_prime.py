import math
def solution(n):
    answer = 0
    for j in range(2, n + 1):
        flag = True
        for i in range(2, int(math.sqrt(j) + 1)):
            if j % i == 0:
                flag = False
                break
        if flag:
            answer += 1
    return answer
print(solution(10))
