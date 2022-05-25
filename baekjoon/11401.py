n, k = map(int, input().split())
p = 1000000007

def factorial(N):
    t = 1
    for i in range(2, N + 1):
        t *= i
        t %= p
    return t

def square(a, b):
    if b == 0:
        return 1

    elif b == 1:
        return a
    
    tmp = square(a, b // 2)
    if b % 2:
        return tmp * tmp * a % p
    else:
        return tmp * tmp % p

top = factorial(n)
bot = factorial(n - k) * factorial(k) % p

print(top * square(bot, p - 2) % p)