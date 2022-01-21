n = int(input())
candy = [0]

for _ in range(n):
    t = list(map(int, input().split()))
    if t[0] == 1:
        candy = sorted(candy)
        print(candy[t[1]])
        candy.pop(t[1])

    if t[0] == 2:
        a, b, c = map(int, t)
        #candy[b] += c
        candy += [b] * c