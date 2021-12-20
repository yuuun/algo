n = int(input())
rope = sorted([int(input()) for _ in range(n)], reverse=True)

pos = []
for i in range(n):
    pos.append(rope[i] * (i + 1))

print(max(pos))