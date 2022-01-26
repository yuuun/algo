n = int(input())
alpha = set(input() for _ in range(n))
print('\n'.join(sorted(alpha, key=lambda x: (len(x), x))))