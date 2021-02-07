# dynamic programming
num_test = int(input())
rgb_list = []

for _ in range(num_test):
    rgb_list.append(list(map(int, input().split())))

#rgb_list: accumulation
for i in range(1, num_test):
    rgb_list[i][0] = min(rgb_list[i - 1][1], rgb_list[i - 1][2]) + rgb_list[i][0]
    rgb_list[i][1] = min(rgb_list[i - 1][0], rgb_list[i - 1][2]) + rgb_list[i][1]
    rgb_list[i][2] = min(rgb_list[i - 1][0], rgb_list[i - 1][1]) + rgb_list[i][2]

print(min(rgb_list[i][0], rgb_list[i][1], rgb_list[i][2]))