def solution(n, m):
    gcd_val = gcd(n, m)
    lcm_val = n * m / gcd_val

    return [gcd_val, int(lcm_val)]

def gcd(n, m):
    a = min(n, m)
    res = 1
    for i in range(a, 1, -1):
        if n % i == 0  and m % i == 0:
            res = i
            break
    return res

print(solution(3, 12))
print(solution(2, 18)) 
print(solution(4, 18))
print(solution(2, 7))