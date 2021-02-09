#dynamic programming

'''
def getList(wine_list):
    ans_list = []
    ans_list.append(wine_list[0])
    ans_list.append(wine_list[0] + wine_list[1])
    ans_list.append(max(wine_list[0], wine_list[1]) + wine_list[2])
    for i in range(3, test_case):
        ans_list.append(max(ans_list[i - 3] + wine_list[i - 1], ans_list[i - 2]) + wine_list[i])
    return max(ans_list[-1], ans_list[-2])
    
test_case = int(input())
wine_list = [0 for i in range(10000)]
for i in range(test_case):
    wine_list[i] = int(input())

tmp1 = getList(wine_list)
tmp2 = getList(wine_list[::-1])
print(max(tmp1, tmp2))
[6, 2, 2, 1, 1, 2, 2]: error
'''

test_case = int(input())
if test_case == 1:
    print(int(input()))
else:
    wine_list = [0]
    for i in range(test_case):
        wine_list.append(int(input()))

    ans_list = [0]
    ans_list.append(wine_list[1])
    ans_list.append(wine_list[1] + wine_list[2])
    for i in range(3, test_case + 1):
        ans_list.append(max(wine_list[i] + wine_list[i - 1] + ans_list[i - 3], wine_list[i] + ans_list[i - 2], ans_list[i - 1]))
        
    print(ans_list[test_case])