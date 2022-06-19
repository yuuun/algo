from collections import deque

n, k = map(int, input().split())
arr = input()
back_cnt = arr.count('T')

if back_cnt == n:
    print(0)
    exit()

def bfs():
    global back_cnt
    visited = [0] * (n + 1)
    q = deque()
    q.append([back_cnt, 0])     #뒤집힌 동전의 개수, k-뒤집기 횟수

    while q:
        bc, kc = q.popleft()
        fc = n - bc
        kc = kc + 1
        for i in range(k + 1):
            turn_back = i
            turn_front = k - i
            
            if turn_back > bc or turn_front > fc: # 뒤집힐 수 있는 개수보다 뒤집을 개수가 클 수가 없음
                continue
            
            back_cnt = bc - turn_back + turn_front

            if back_cnt == n:
                return kc
            
            if visited[back_cnt]:
                continue
            visited[back_cnt] = 1
            q.append([back_cnt, kc])
    return -1

print(bfs())