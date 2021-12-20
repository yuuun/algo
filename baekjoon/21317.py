n = int(input())
power = [0] + [list(map(int, input().split())) for _ in range(n - 1)]
big = int(input())
arr = []

def sol(cur, used, ans):
    if cur == n:
        arr.append(ans)
        return
    if cur > n:
        return
    if not used:
        sol(cur + 3, True, ans + big)
    
    sol(cur + 1, used, ans + power[cur][0])
    sol(cur + 2, used, ans + power[cur][1])

sol(1, False, 0)
print(min(arr))

'''
이 방법은 한 번만 매우 큰 점프를 했다는 정보를 포함하고 있지 않음
dp = [5000] * (n + 3)
dp[0] = 0
for idx, po in enumerate(power):
    dp[idx + 1] = min(dp[idx] + po[0], dp[idx + 1])
    dp[idx + 2] = min(dp[idx] + po[1], dp[idx + 2])
    dp[idx + 3] = min(dp[idx] + big, dp[idx + 3])

print(dp[n - 1])
'''