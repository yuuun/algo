from collections import defaultdict
def solution(k, room_number):
    visited = defaultdict(list)
    answer = []
    for room in room_number:
        if room not in visited:
            visited[room] = [room]
            answer.append(room)
            continue
        t = visited[room][-1]
        while t in visited:
            t += 1
        for r in visited[room]:
            visited[r].append(t)
        answer.append(t)
    return answer
print(solution(10, [1, 3, 4, 1, 3, 1]))


def solution2(k, room_number):
    answer = []
    room = {}
    for num in room_number:
        number = room.get(num, 0)
        if number :
            temp = [num]
            while True:
                index = number
                number = room.get(number, 0)
                if not number:
                    answer.append(index)
                    room[index] = index + 1
                    for i in temp:
                        room[i] = index + 1
                    break
                temp.append(number)
        else:
            answer.append(num)
            room[num] = num + 1
    return answer


print(solution2(10, [1, 3, 4, 1, 3, 1]))