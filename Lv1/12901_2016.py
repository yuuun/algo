def solution(a, b):
    days = 4 + b
    #한 달에 있는 일수 저장하는 arr
    if(a > 1):
        days_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        for i in range(a-1):
            days += days_list[i]
    str_day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    return str_day[days % 7]
print(solution(5, 24))