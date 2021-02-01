def solution(d, budget):
    d.sort()
    cnt = 0
    while cnt < len(d) and budget - d[cnt] >= 0:
        budget -= d[cnt]
        cnt += 1
    return cnt

print(solution([1,3,2,5,4], 9))

print(solution([2,2,3,3], 10))
