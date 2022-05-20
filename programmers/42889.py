from collections import Counter
def solution(N, stages):
    tot = len(stages)
    answer = []
    cnt = Counter(stages)
    for i in range(1, N + 1):
        if tot == 0:
            answer.append(0)
            continue
        answer.append(cnt[i] / tot)
        tot -= cnt[i]
    answer = sorted(range(len(answer)), key=lambda k: -answer[k])
    for i in range(N):
        answer[i] += 1
    return answer