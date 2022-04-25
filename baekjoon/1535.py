n = int(input())
power = list(map(int, input().split()))
good = list(map(int, input().split()))
dp = []
max_val = 0
for p, g in zip(power, good):
    for pd, gd in dp[:len(dp)]:
        if pd + p < 100:
            max_val = max(g + gd, max_val)
            dp.append([pd + p, g + gd])
    if p < 100:
        max_val = max(g, max_val)
        dp.append([p, g])
print(max_val)

'''
N = int(input()) 
L = [int(x) for x in input().split()] 
J = [int(x) for x in input().split()] 
L, J = [0] + L, [0] + J 
dp = [[0 for _ in range(101)] for _ in range(N+1)] 
for i in range(1, N+1): 
    for j in range(1, 101): 
        if L[i] <= j: 
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-L[i]] + J[i]) 
        else: 
            dp[i][j] = dp[i-1][j] 
print(dp[N][99])

'''