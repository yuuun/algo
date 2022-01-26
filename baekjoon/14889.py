from itertools import combinations
n = int(input())
scores = [list(map(int, input().split())) for _ in range(n)]

possible = []
for pos in list(combinations(list(range(n)), n // 2)):
    possible.append(pos)

min_val = 10000
def get_score(x):
    score = 0
    for j in range(n // 2):
        m = x[j]
        for k in x:
            score += scores[m][k]
    return score

for pos in range(len(possible) // 2):
    min_val = min(min_val, abs(get_score(possible[pos]) - get_score(possible[-pos - 1])))

print(min_val)