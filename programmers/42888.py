from collections import defaultdict
def solution(record):
    name = defaultdict(str)
    answer = []
    for re in record:
        re = re.split(' ')
        if len(re) == 2:
            answer.append([re[1], '님이 나갔습니다.'])
        else:
            name[re[1]] = re[2]
            if re[0] == 'Enter':
                answer.append([re[1], '님이 들어왔습니다.'])
    for i in range(len(answer)):
        answer[i] = name[answer[i][0]] + answer[i][1]
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]), ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."])