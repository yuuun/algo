def change_list(s):
    s = [t[1:].split(',') for t in s[1:-2].split('},')]
    return s
def solution(s):
    s = change_list(s)
    s = sorted(s, key=lambda x: len(x))
    res = []
    for st in s:
        for t in st:
            if t not in res:
                res.append(t)
    return list(map(int, res))

from collections import Counter
import re
def solution2(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"), [2, 1, 3, 4])