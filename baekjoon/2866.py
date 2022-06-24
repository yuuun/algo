## TBD
from collections import deque
n, m = map(int, input().split())
arr = deque()

for _ in range(n):
    tmp = list(input())
    for j in range(m):
        tmp[j] = ord(tmp[j]) - 97
    arr.append(tmp)

def isPass():
    global arr
    idx = 1
    for i in range(m):
        tmp = 0
        for j in range(len(arr)):
            k = 1 << arr[j][i]
            if tmp & k:
                return i + 1
            else:
                tmp |= k
    return False
            
while arr:
    idx = isPass()
    if idx:
        print()