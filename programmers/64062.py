#TBD - 시간초과
def check(stones, k):
    cnt = 1
    for i, s in enumerate(stones):
        if s > 0:
            stones[i] -= 1
            cnt = 1
        else:
            cnt += 1
            if cnt > k:
                return stones, False
    return stones, True

def solution(stones, k):
    answer = 0
    while True:
        stones, isTrue = check(stones, k)
        if not isTrue:
            break
        answer += 1
    return answer
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))