#완전 탐색
from itertools import permutations
def isPrime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    numbers = [k for k in numbers]
    n = len(numbers)
    candidate = set()
    for i in range(1, n + 1):
        comb = permutations(numbers, i)
        for tmp in comb:
            tmp = ''.join(map(str, list(tmp)))
            candidate.add(int(tmp))
    answer = 0
    for can in candidate:
        if isPrime(can):
            answer += 1
    return answer
