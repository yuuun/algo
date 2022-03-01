a, b = map(int, input().split())
b += int(input())
t_a, b = b // 60, b % 60
a += t_a
a = a % 24

print(a, b)