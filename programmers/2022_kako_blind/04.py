def solution(n, info):
    global answer, point
    answer = [-1]
    point = 0 # 가장 높은 점수를 가질 경우를 결과로 내야 하기 떄문
    
    def dfs(idx, n, lion):
        global answer, point
        if n < 0:
            return
        if idx > 10:
            lion_score, apeach_score = 0, 0
            for idx in range(11):
                if lion[idx] == info[idx] == 0:
                    continue
                if lion[idx] > info[idx]:
                    lion_score += 10 - idx
                else:
                    apeach_score += 10 - idx
            
            if lion_score > apeach_score:
                sub_score = lion_score - apeach_score
                if sub_score > point:
                    point = sub_score
                    answer = [l for l in lion]
                    answer[-1] += n
            return
            
                
        lion[10 - idx] = info[10 - idx] + 1
        dfs(idx + 1, n - lion[10 - idx], lion)
        lion[10 - idx] = 0
        dfs(idx + 1, n, lion)
        
    dfs(0, n, [0] * 11)
    return answer