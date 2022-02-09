# https://programmers.co.kr/learn/courses/30/lessons/92335
def solution(n, k):
    p = []
    while n > 0:
        p.append(n % k)
        n //= k
    p = ''.join(map(str, p[::-1])).split('0')
    p = [int(x) for x in p if x != '']    
    
    # 소수 찾기
    def find_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    answer = 0
    for n in p:
        isPrime = find_prime(n)
        if isPrime:
            answer += 1
            
    return answer