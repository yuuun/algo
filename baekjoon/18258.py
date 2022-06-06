import sys
from collections import deque
q = deque()
for _ in range(int(input())):
    tmp = sys.stdin.readline().split()
    if tmp[0] == 'push':
        q.append(tmp[1])
    else:
        if tmp[0] == 'pop':
            if q:
                print(q.popleft())
            else:
                print(-1)
        elif tmp[0] == 'size':
            print(len(q))
        elif tmp[0] == 'empty':
            if len(q) == 0:
                print(1)
            else:
                print(0)
        elif tmp[0] == 'front':
            if q:
                print(q[0])
            else:
                print(-1)
        else:
            if q:
                print(q[-1])
            else:
                print(-1)