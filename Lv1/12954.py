def solution(x, n):
    return list(i * x for i in range(1, 1 + n))
    
print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))