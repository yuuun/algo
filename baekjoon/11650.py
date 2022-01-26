n = int(input())
pos = [list(map(int, input().split())) for _ in range(n)]

pos = sorted(pos, key=lambda x: (x[0], x[1]))

for p in pos:
    print(' '.join(map(str, p)))
