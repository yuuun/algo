#처음에 심판의 기대치보다 더 작은 점수를 가진 것 중 최댓값을 가지는 값을 가지는 경기가 최대인 줄 알아서 잘못 품
#자신의 기준에 맞는 경기 중 가장 작은 인덱스를 가지는 경기를 좋아함
#구현
n, m = map(int, input().split())
A = [int(input()) for _ in range(n)]
B = [int(input()) for _ in range(m)]

score = [0 for _ in range(n)]

for b in B:
    for idx, a in enumerate(A):
        if b >= a:
            score[idx] += 1
            break
print(score.index(max(score)) + 1)