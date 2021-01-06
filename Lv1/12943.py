def solution(num):
    cnt = 0
    while num != 1 and cnt < 500:
        n = num / 2
        cnt += 1
        if n.is_integer():
            num = n
        else:
            num = 3 * num + 1
    if cnt == 500:
        return -1
    else:
        return cnt
        
print(solution(16))
print(solution(626331))