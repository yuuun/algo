n, k = map(int, input().split())
stone = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    for j in range(i - 1, 0, -1):
        tmp = (i - j) * (1 + abs(stone[j] - stone[i]))
        if tmp <= k:
            dp[i] = dp[j] + tmp
isTrue = False
for i in range(n):
    for j in range(i - 1, 0, -1):
        if (i - j) * (1 + abs(stone[j] - stone[i])) <= k:
            break
    if i == n - 1:
        isTrue = True

if dp[-1] == 1:
    print('YES')
else:
    print('NO')

'''### 시간 초과
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
    '''