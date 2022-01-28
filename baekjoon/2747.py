n = int(input())
if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    print(b)