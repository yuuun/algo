n = int(input())
if n == 1:
    print(1)
else:
    a, b = 1, 2
    for _ in range(n - 2):
        a, b = b, a + b
    print(b % 10007)