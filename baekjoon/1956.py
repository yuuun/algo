n = int(input())
inp = list(map(int, input().split()))
dp = [1 for _ in range(n)]
for idx in range(1, n):
    tmp = []
    for idx2 in range(0, idx):
        if inp[idx2] < inp[idx]:
            tmp.append(dp[idx2])
    if tmp:
        dp[idx] = max(tmp) + 1

print(max(dp))