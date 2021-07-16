def solution(triangle):
    triangle.reverse()
    for idx, tri in enumerate(triangle[:-1]):
        for idx2 in range(len(tri) - 1):
            triangle[idx + 1][idx2] += max(triangle[idx][idx2], triangle[idx][idx2 + 1])
    answer = triangle[-1][0]
    return answer
