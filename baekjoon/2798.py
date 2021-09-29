from itertools import permutations
n, m = map(int, input().split())
cards = list(map(int, input().split()))

permute = permutations(cards, 3)

ans = 0
for per in permute:
    sum_per = sum(per)
    if m + 1 > sum_per:
        ans = max(ans, sum_per)
print(ans)