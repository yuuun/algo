def solution(prices):
    answer = []
    for i in range(len(prices) - 1):
        cnt = 0
        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                break
            cnt += 1
        if cnt == 0:
            cnt += 1
        answer.append(cnt)
    answer.append(0)
    return answer

print(solution([2, 3, 2, 1]))