n = int(input())
t = 0
for i in range(1, n + 1):
    if n % i == 0:
        t += i
print(t * 5 - 24)