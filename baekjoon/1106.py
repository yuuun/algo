c, n = map(int, input().split())
cust = []

for _ in range(n):
    cust.append(list(map(int, input().split())))

ans = [0] * (101 + C)
for money, customer in cust:
    for cur in range(customer, C + 101):
        dp[cur] = min(dp[cur], dp[cur - customer] + cost)

print(min(dp[C:C+101]))