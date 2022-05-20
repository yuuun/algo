def combination(arr, k):
    for i in range(len(arr)):
        if k == 1:
            yield [arr[i]]
        else:
            for j in combination(arr[i + 1:], k - 1):
                yield [arr[i]] + j
def solution(relation):
    n = len(relation[0])
    key_idx = list(range(n))
    candidate = []
    for i in range(1, n + 1):
        for comb in combination(key_idx, i):
            hist = []
            for rel in relation:
                current = [rel[c] for c in comb]
                if current in hist:
                    break
                else:
                    hist.append(current)
            else:
                for ck in candidate:
                    if set(ck).issubset(set(comb)):
                        break
                else:
                    candidate.append(comb)

    return len(candidate)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]), 2)