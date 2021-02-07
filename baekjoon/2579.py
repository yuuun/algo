#dynamic programming
num_test = int(input())
stairs = [0 for i in range(301)]  #num_test=1 or 2인 경우 9, 10번째에서 오류 날 수 있기 때문에 고려할 것
for i in range(num_test):
    stairs[i] = int(input())

sum_stair = []
sum_stair.append(stairs[0])
sum_stair.append(stairs[0] + stairs[1])
sum_stair.append(max(stairs[0], stairs[1]) + stairs[2])

for i in range(3, num_test):
    sum_stair.append(max(sum_stair[i - 3] + stairs[i - 1], sum_stair[i - 2]) + stairs[i])
print(sum_stair[num_test - 1])
print(sum_stair)