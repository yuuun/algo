T = int(input())
for test_case in range(1, T + 1):
    t = int(input())
    scores  = list(map(int, input().split()))
    li = [0] * 101
    for sc in scores:
        li[sc] += 1
    max_score = 1
    for i in range(101):
        if li[i] >= max_score:
            max_index = i
            max_score = li[i]
    print('#{} {}'.format(test_case, max_index))