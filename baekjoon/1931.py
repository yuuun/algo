#greedy
'''input'''
n_meeting = int(input())

meeting_list = []

for i in range(n_meeting):
    meeting_list.append(list(map(int, input().split())))
    
#회의 시간을 끝나는 시간으로 먼저 sorting한 뒤, 시작하는 시간으로 sorting한다.
meeting_list = sorted(meeting_list, key = lambda x : (x[1], x[0]))

cnt = 1     #특정시간까지의 회의 개수
idx = 0     #meeting의 index
end_point = meeting_list[idx][1]    #첫번째 회의가 끝나는 시간

while idx < n_meeting - 1:
    idx += 1
    #앞선 미팅의 끝나는 시간 이후에 시작하는 시간일 경우 meeting이 시작됨
    if meeting_list[idx][0] >= end_point: 
        cnt += 1
        end_point = meeting_list[idx][1]   #마지막 회의 시간을 update
print(cnt)


''' 시간 초과
for idx, ml in enumerate(meeting_list):
    for idx2, ml2 in enumerate(meeting_list[idx + 1:]):
        if ml2[0] >= end_point:
            cnt += 1
            end_point = ml2[1]
            break
    if idx < idx2:
        continue
'''
