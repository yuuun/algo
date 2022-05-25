def solution(msg):
    dic = {}
    for i in range(1, 27):
        dic[chr(64 + i)] = i
    
    idx = 27
    answer = []
    k = 0
    while k < len(msg):
        tmp = msg[k]
        k += 1
        while k < len(msg):
            tmp += msg[k]
            k += 1
            if tmp not in dic:
                dic[tmp] = idx
                k -= 1
                break
        if k < len(msg):
            answer.append(dic[tmp[:-1]])
            idx += 1
        else:
            answer.append(dic[tmp])
    return answer


print(solution('KAKAO'),	[11, 1, 27, 15])
print(solution('TOBEORNOTTOBEORTOBEORNOT'),	[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34])
print(solution('ABABABABABABABAB'),	[1, 2, 27, 29, 28, 31, 30])