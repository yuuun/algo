def permutation(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for j in permutation(arr[:i] + arr[i + 1:], r - 1):
                yield [arr[i]] + j

def solution(k, dungeons):
    answer = -1
    for dug in permutation(dungeons, len(dungeons)):
        tmp = 0
        full = k
        for a, b in dug:
            if full >= a:
                full -= b
                tmp += 1
            else:
                break
        answer = max(answer, tmp)
    return answer