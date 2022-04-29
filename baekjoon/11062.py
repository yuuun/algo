def get_score(turn, i, j):
    if i > j:
        return 0
    if dp[i][j]:
        return dp[i][j]
    
    # 근우
    if turn:
        score = max(get_score(False, i + 1, j) + lis[i], get_score(False, i, j - 1) + lis[j])
        dp[i][j] = score
        return score
    else:
        score = min(get_score(True, i + 1, j), get_score(True, i, j - 1))
        dp[i][j] = score
        return score

for _ in range(int(input())):
    t = int(input())
    lis = list(map(int, input().split()))
    dp = [[0] * t for _ in range(t)]
    get_score(True, 0, t - 1)
    print(dp[0][-1])
    