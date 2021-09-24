t = int(input())
dp = [0, 1, 2, 4]

for _ in range(t):
    inp = int(input())
    len_dp = len(dp) - 1
    if inp < len_dp:
        print(dp[inp])
    else:
        for i in range(len_dp, inp):
            dp.append(dp[i] + dp[i - 1] + dp[i - 2])
        
        print(dp[-1])