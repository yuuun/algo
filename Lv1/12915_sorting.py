import numpy as np
def solution(strings, n):
    arr = np.argsort(list(s[n] for s in strings))
    
    answer = []
    
    tmp = []
    for idx in range(1, len(arr)):
        if strings[arr[idx]] == strings[arr[idx - 1]]:
            tmp.append(True)
        else:
            tmp.append(False)
    sidx = 0
    eidx = 1
    for t in tmp:
        if t:
            eidx += 1
        else:
            answer = answer + strings[arr[sidx: eidx]]
            sidx = eidx



    return answer

print(solution(['sun', 'bed', 'car'], 1))
print(solution(['abce', 'abcd', 'cdx'], 2))