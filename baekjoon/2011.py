letter = list(map(int, list(input())))
if letter[0] == 0:
    print(0)
else:
    dp = [0] * (len(letter) + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, len(letter) + 1):
        if letter[i - 1] > 0:
            dp[i] = dp[i - 1]
        n = letter[i - 1] + letter[i - 2] * 10
        if 10 <= n and n <= 26:
            dp[i] += dp[i - 2]
    print(dp[-1] % 1000000)