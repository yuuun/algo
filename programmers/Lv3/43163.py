#bfs
from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [False for _ in range(len(words))]
    q = deque()
    q.append([begin, 0])
    isTrue = False
    while q:
        t = q.popleft()
        st, val = t[0], t[1]
        
        if st == target:
            isTrue = True
            return val
          
        for idx in range(len(st)):
            tmp1 = st[:idx] + st[idx + 1:]
            for idx2, wo in enumerate(words):
                tmp2 = wo[:idx] + wo[idx + 1:]
                if tmp1 == tmp2 and not visited[idx2]:
                    visited[idx2] = True
                    q.append([wo, val + 1])
                    
    if not isTrue:
        return 0
