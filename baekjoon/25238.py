a, b = map(int, input().split())
print(0 if a * (100 - b) * 0.01 >= 100 else 1)