n = int(input())
a, b = map(int, input().split())
a //= 2
print(min(n, a + b))