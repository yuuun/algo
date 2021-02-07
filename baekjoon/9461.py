#dynamic programming
num_test = int(input())

for t in range(num_test):
    val = int(input())
    ans_list = [1, 1, 1]
    for i in range(3, val):
        ans_list.append(ans_list[i - 2] + ans_list[i - 3])
    print(ans_list[val - 1])