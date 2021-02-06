
def solve(computers, node, visited, cur):    
    if visited[node] == 0:
        cur += 1
    comp = computers[node]
    for idx, c in enumerate(comp):
        if comp[idx] == 1 and visited[idx] == 0:
            visited[idx] = cur
            visited, cur = solve(computers, idx, visited, cur)
    
    return visited, cur
         
def solution(n, computers):
    visited = [0 for i in range(n)]
    cur = 0
    for idx in range(n):
        visited, cur = solve(computers, idx, visited, cur)
    return max(visited)