from collections import deque
q = deque()
cnt = 1
m = int(input())
ans = []
flag = True
for _ in range(m):
    n  = int(input())
    while cnt <= n:
        ans.append('+')
        q.append(cnt)
        cnt += 1
    
    if q[-1] == n:
        ans.append('-')
        q.pop()
    else:
        flag = False
if flag:
    print('\n'.join(ans))
else:
    print('NO')