n = int(input())
a, b = 1, 0
b = 0
for _ in range(n):
    a, b = b, a + b
print(a, b)