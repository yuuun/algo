from itertools import combinations
tmp = list(map(int, input().split()))
while tmp != [0]:
    k = tmp[0]
    case = tmp[1:]
    candidate = list(combinations(case, 6))
    for can in candidate:
        print(' '.join(map(str, list(can))))
    print()
    tmp = list(map(int, input().split()))