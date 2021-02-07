#dynamic programming
num_test = int(input())

train_list = []
for _ in range(num_test):
    train_list.append(list(map(int, input().split())))

for idx in range(1, num_test):
    train_list[idx][0] += train_list[idx - 1][0]
    train_list[idx][-1] += train_list[idx - 1][-1]
    for t in range(1, len(train_list[idx]) - 1):
        train_list[idx][t] += max(train_list[idx - 1][t], train_list[idx - 1][t - 1])
        
print(max(train_list[-1]))