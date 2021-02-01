a, b = map(int, input().split())
min_val = min(a, b)
max_val = max(a, b)
print(max_val - min_val + 1)