#완전 탐색
def divisor(num):
    tmp = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            tmp.append([i, num // i])
    return tmp
def solution(brown, yellow):
    candidate = divisor(brown + yellow)
    for can1, can2 in candidate:
        if (can1 + can2) * 2 == brown + 4:
            return [can2, can1]
