# fees = [기본시간, 기본요금, 단위시간, 단위요금]
# recodes[0] = [시각, 차량번호, 입차여부]
import math
from collections import defaultdict
def solution(fees, records):
    def calculate_time(x, y):
        x = list(map(int, x.split(':')))
        y = list(map(int, y.split(':')))
        return (y[0] - x[0]) * 60 + y[1] - x[1]
    
    def calculate_money(time):
        if time <= fees[0]:
            return fees[1]
        return fees[1] + fees[3] * math.ceil((time - fees[0]) / fees[2])
    
    dic = {}
    time_dic = defaultdict(int)
    for re in records:
        time, num, isOut = re.split(' ')
        if isOut == 'IN':
            dic[num] = time
        else:
            time_dic[num] += calculate_time(dic[num], time)
            del dic[num]
    # 일괄 출차        
    for num, time in dic.items():
        time_dic[num] += calculate_time(time, '23:59')
        
    answer = []
    for num, time in sorted(time_dic.items()):
        answer.append(calculate_money(time))
        
    return answer