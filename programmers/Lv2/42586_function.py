import math
def solution(progresses, speeds):
    days = []
    for prog, spe in zip(progresses, speeds):
        remain = 100 - prog
        days.append(math.ceil(remain / spe))
        
    prevDay = days[0]
    answer = [1]
    
    for day in days[1:]:
        if day <= prevDay:
            answer[-1] += 1
        else:
            answer.append(1)
            prevDay = day
    return answer
        

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))