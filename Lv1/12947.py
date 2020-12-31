def solution(x):
    sumX = sum(list(map(int, str(x))))
    if (x / sumX).is_integer():
        return "true"
    else:
        return "false"
print(solution(12))