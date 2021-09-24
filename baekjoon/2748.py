n = int(input())
a, b = 0, 1
tmp = 0
for i in range(n):
    tmp = a
    a = b
    b = tmp + b
print(a)