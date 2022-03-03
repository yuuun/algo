from collections import defaultdict
ans = 0

def solution(info, edges):
    global visited
    dics = defaultdict(set)
    for a, b in edges:
        dics[a].add(b)
    
    def dfs(cur, n_sheep, n_wolf, next_list):
        global ans

        if info[cur] == 0:
            n_sheep += 1
            ans = max(ans, n_sheep)
        else:
            n_wolf += 1

        if n_sheep > n_wolf:
            next_list.update(dics[cur])
            for next in next_list:
                dfs(next, n_sheep, n_wolf, next_list - set([next]))
        else:
            return
    
    dfs(0, 0, 0, set())
    return ans

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))