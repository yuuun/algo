#dynamic programming
test_case = int(input())
ans = [[0 for i in range(10)] for j in range(301)]
for i in range(1, 10):
    ans[1][i] = 1
for i in range(2, test_case + 1):
    ans[i][0] = ans[i - 1][1]
    ans[i][9] = ans[i - 1][8]
    for j in range(1, 9):
        ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j + 1]
print(sum(ans[test_case]) %1000000000)