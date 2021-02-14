#greedy
n, k = map(int, input().split())

coin_list = []
for i in range(n):
    coin_list.append(int(input()))

cnt = 0
for coin in coin_list[::-1]:
    if coin > k:
        continue
    else:
        cnt += int(k / coin)
        k = k % coin
print(cnt)