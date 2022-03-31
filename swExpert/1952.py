def solution(n, cnt):
    global ans
    if n > 11:
        ans = min(ans, cnt)
        return
    solution(n + 1, cnt + month_price[n])
    solution(n + 3, cnt + price[2])

t = int(input())
for j in range(1, t + 1):
    price = list(map(int, input().split()))
    days = list(map(int, input().split()))
    ans = price[-1]
    # 월 변경
    month_price = []
    for i in range(12):
        days_ = days[i] * price[0]
        month_price.append(min(days_, price[1]))
    
    solution(0, 0)
    print('#{0} {1}'.format(j, ans))