def solution(num):
    half = num / 2
    if half.is_integer():
        return "Even"
    else:
        return "Odd"
print(solution(3))