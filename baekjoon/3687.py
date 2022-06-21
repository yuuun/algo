from collections import defaultdict
arr = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]
def getMax(x):
    ret = [1] * (x // 2)
    if x & 1:
        ret[0] = 7
    return ''.join(map(str, ret))

def getMin(x):
    ret = [8] * ((x + 6) // 7)
    k = x % 7
    if k == 1:
        ret[0] = 1
        ret[1] = 0
    elif k == 2:
        ret[0] = 1
    elif k == 3:
        ret[0] = 2
        ret[1] = 0
        ret[2] = 0
    elif k == 4:
        ret[0] = 2
        ret[1] = 0
    elif k == 5:
        ret[0] = 2
    elif k == 6:
        ret[0] = 6
    return ''.join(map(str, ret))

for _ in range(int(input())):
    t = int(input())
    if t < 11:
        print(arr[t], end=' ')
    else:
        print(getMin(t))
    print(getMax(t))