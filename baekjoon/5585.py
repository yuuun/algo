#greedy
val = 1000 - int(input())

money_list = [500, 100, 50, 10, 5, 1]

cnt = 0
for ml in money_list:
    while val >= ml:
        val -= ml
        cnt += 1

print(cnt)