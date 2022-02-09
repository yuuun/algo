### Level 1 https://programmers.co.kr/learn/courses/30/lessons/92334
from collections import defaultdict
def solution(id_list, report, k):
    report = list(set(report)) # 동일한 신고는 한번으로
    dic = defaultdict(int)
    for re in report:
        x, y = re.split(' ')
        dic[y] += 1
    
    peo = []
    for key, value in dic.items():
        if value >= k:
            peo.append(key)
    
    answer = [0] * len(id_list)
    for re in report:
        x, y = re.split(' ')
        if y in peo:
            answer[id_list.index(x)] += 1
            
    return answer