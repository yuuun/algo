#처음에 pop를 이용하여 list의 수를 줄이는 식으로 하였는데 효율성 테스트에서 통과하지 못함
def solution(people, limit):
    people = sorted(people)
    start = 0
    end = len(people) - 1
    answer = 0
    while end - start >= 1:
        if people[end] + people[start] > limit:
            end -= 1
        else:
            start += 1
            end -= 1
        answer += 1
    if end == start:
        answer += 1
    return answer


if __name__=="__main__":
    print(solution([70, 50, 80, 50], 100))