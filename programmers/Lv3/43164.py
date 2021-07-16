#TBD
def dfs(cur, tickets, visited, ans):
    for idx, tick in enumerate(tickets):
        if cur == tick[0] and not visited[idx]:
            visited[idx] = True
            ans.append(tick[1])
            dfs(tick[1], tickets, visited, ans)
    return ans             

def solution(tickets):
    tickets = sorted(tickets, key=lambda x: (x[0], x[1]))
    visited = [False for _ in range(len(tickets))]
    return dfs("ICN", tickets, visited, ["ICN"])
