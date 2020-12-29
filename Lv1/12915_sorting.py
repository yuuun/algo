import numpy as np
def solution(strings, n):
    arr = np.argsort(list(s[n] for s in strings))
        
    return list(strings[a] for a in arr)

print(solution(['sun', 'bed', 'car'], 1))
print(solution(['abce', 'abcd', 'cdx'], 2))