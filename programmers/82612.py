def solution(price, money, count):
    tmp = price * (count) * (count + 1) // 2
    answer = tmp - money
    if answer < 0:
        return 0
    return answer

print(solution(3, 20, 4), 10)