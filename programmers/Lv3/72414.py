def str_to_second(time):
    time = list(map(int, time.split(':')))
    return 3600 * time[0] + 60 * time[1] + time[2]

def second_to_str(time):
    h = str(time // 3600).zfill(2)
    m = str(time % 3600 // 60).zfill(2)
    s = str(time % 3600 % 60).zfill(2)
    
    return h + ':' + m + ':'+ s

def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return '00:00:00'
    
    play_time = str_to_second(play_time)
    adv_time = str_to_second(adv_time)
    total_time = [0] * (play_time + 1)

    for l in logs:
        s, e = l.split('-')
        s = str_to_second(s)
        e = str_to_second(e)
        total_time[s] += 1
        total_time[e] -= 1
    
    # 누적합
    # 각 구간에서 틀어져 있는 tv개수
    for i in range(1, play_time):
        total_time[i] = total_time[i] + total_time[i - 1]
    # 현 시점까지의 누적 시간 계산
    for i in range(1, play_time):
        total_time[i] = total_time[i] + total_time[i - 1]
    
    max_val = -1
    time = 0
    for i in range(adv_time - 1, play_time):
        tmp = total_time[i] - total_time[i - adv_time]
        if tmp > max_val:
            max_val = tmp
            time = i - adv_time + 1
    return second_to_str(time)
            

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59",	"25:00:00",	["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))