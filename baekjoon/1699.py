# 틀렸습니다....!!!!!!!! 수정할 것
import math
n = int(input())
sqr = [i * i for i in range(int(math.sqrt(n)), 0, -1)]

cnt = 0
for s in sqr:
    while n >= s:
        n -= s
        cnt += 1
    
print(cnt)