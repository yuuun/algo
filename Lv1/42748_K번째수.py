def solution(array, commands):
    answer = []
    for coms in commands:
        #idx는 0부터 시작하기 때문에 하나 빼주는 곳에서부터 시작
        tmp = array[coms[0] - 1 : coms[1]]
        tmp.sort()
        answer.append(tmp[coms[2]-1])        
    return answer

print(solution([1,5,2,6,3,7,4], [[2,5,3], [4,4,1], [1,7,3]]))