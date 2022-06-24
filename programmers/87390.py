def solution(n, left, right):
    xu, xd = left // n, left % n
    right += 1
    yu, yd = right // n, right % n
    answer = []
    # 1
    if xu == yu:
        for i in range(xd, yd):
            if xu < i:
                answer.append(i + 1)
            else:
                answer.append(xu + 1)
        return answer
    else:
        for i in range(xd, n):
            if xu < i:
                answer.append(i + 1)
            else:
                answer.append(xu + 1)
    # 2
    for j in range(xu + 1, yu):
        for i in range(n):
            if j < i:
                answer.append(i + 1)
            else:
                answer.append(j + 1)
    # 3
    for i in range(yd):
        if yu < i:
            answer.append(i + 1)
        else:
            answer.append(yu + 1)
    return answer
print(solution(3, 2, 5), [3, 2, 2, 3])
print(solution(4, 7, 14), [4, 3, 3, 3, 4, 4, 4, 4])
print(solution(4, 5, 14), [2, 3, 4, 3, 3, 3, 4, 4, 4, 4])