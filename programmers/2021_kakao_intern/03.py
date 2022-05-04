from collections import deque

def solution2(n, k, cmd):
    exists = [True for _ in range(n)]
    up = [-1] + [x for x in range(n - 1)]
    down = [x for x in range(1, n)] + [-1]
    q = deque()
    
    for c in cmd:
        op = c[0]
        
        if op == 'U':
            val = int(c.split()[1])
            for _ in range(val):
                k = up[k]
                
        elif op == 'D':
            val = int(c.split()[1])
            for _ in range(val):
                k = down[k]
                
        elif op == 'C':
            if up[k] != -1:
                down[up[k]] = down[k]
            if down[k] != -1:
                up[down[k]] = up[k]
            exists[k] = False
            q.append(k)
            k = down[k] if down[k] != -1 else up[k]
            
        else:
            d = q.pop()
            if up[d] != -1:
                down[up[d]] = d
            if down[d] != -1:
                up[down[d]] = d
            exists[d] = True
            
    
    return ''.join(['O' if x else 'X' for x in exists])







print(solution2(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]), 'OOOOXOOO')
print(solution2(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]), "OOXOXOOO")


def solution(n, k, cmd):
    q = deque()
    visited = [False] * n
    for d in cmd:
        d = list(d.split(' '))
        if d[0] == 'D':
            d[1] = int(d[1])
            t = 0
            while t < d[1]:
                if not visited[k]:
                    t += 1
                k += 1
            while visited[k]:
                k += 1
        elif d[0] == 'U':
            d[1] = int(d[1])
            t = 0
            while t < d[1]:
                if not visited[k]:
                    t += 1
                k -= 1
            while visited[k]:
                k -= 1
        elif d[0] == 'C':
            visited[k] = True
            q.append(k)
            if k == n - 1:
                while visited[k]:
                    k -= 1
            else:
                while visited[k]:
                    k += 1
        else:
            visited[q.pop()] = False
    
    answer = ''
    for v in visited:
        if v:
            answer += 'X'
        else:
            answer += 'O'
    return answer