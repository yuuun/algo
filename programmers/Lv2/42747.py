def solution(citations):
    citations = sorted(citations)
    if citations[-1] == 0:
        return 0
    for i in range(len(citations)):
        cnt = 1
        # print(i, citations[i])
        for j in range(len(citations) - 1, i, -1):
            if citations[j] < citations[i]:
                break
            cnt += 1
        if cnt <= citations[i]:
            return cnt

print(solution([3, 0, 6, 1, 5]))
print(solution([0, 0, 0, 0]))