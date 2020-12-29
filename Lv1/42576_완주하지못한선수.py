def solution(participant, completion):
    participant.sort()
    completion.sort()

    for idx in range(len(completion)):
        #participant가 completion보다 항상 하나 많기 때문에 바로 return문
        if participant[idx] != completion[idx]:
            return participant[idx] 
    #마지막의 participant일 경우 바로 대입
    return participant[-1]

print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))