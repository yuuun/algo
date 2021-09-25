### 시간 초과

n, k = map(int, input().split())
stone = list(map(int, input().split()))
istrue = False

def sol(idx):
    global istrue
    if istrue:
        return
    if idx == n - 1:
        istrue = True
        return 
    if idx > n - 1:
        return 
    
    for i in range(idx + 1, n):
        if (i - idx) * (1 + abs(stone[idx] - stone[i])) <= k:
            sol(i)

sol(0)
if istrue:
    print('YES')
else:
    print('NO')