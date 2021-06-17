#greedy algorithm
num = int(input())

pos_list = []
neg_list = []

n_1 = 0
for _ in range(num):
    n = int(input())
    if n > 1:
        pos_list.append(n)
    elif n == 1:    #1일 경우 곱하는 것보다 더하는 것이 더 좋음
        n_1 += 1
    elif n < 0:
        neg_list.append(n)
ans = n_1        
pos_list.sort(reverse=True)
neg_list.sort()

for idx in range(0, len(pos_list) - 1, 2):
    ans += pos_list[idx] * pos_list[idx + 1]
if len(pos_list) % 2 == 1:
    ans += pos_list[-1]
    
for idx in range(0, len(neg_list) - 1, 2):
    ans += neg_list[idx] * neg_list[idx + 1]

if num == (len(pos_list) + len(neg_list) + n_1):
    if len(neg_list) % 2 == 1:
        ans += neg_list[-1]

print(ans)