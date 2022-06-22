n, k = map(int, input().split())
def fac(x):
    t = 1
    for i in range(x - k + 1, x):
        t *= i
    return t

print(fac(n + k) // fac(k) % 1000000000)