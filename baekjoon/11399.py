#greedy algorithm
n = int(input())
num_list = list(map(int, input().split()))

num_list.sort()
cnt = 0
for idx, num in enumerate(num_list):
    cnt += (n - idx) * num
print(cnt)