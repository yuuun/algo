def solution(arr1, arr2):
    n, m, l = len(arr1), len(arr2), len(arr2[0])
    answer = []
    for i in range(n):
        tmp_arr = []
        for k in range(l):
            tmp = 0
            for j in range(m):
                tmp += arr1[i][j] * arr2[j][k]
            tmp_arr.append(tmp)
        answer.append(tmp_arr)
    return answer

print(solution([[1, 4], [3, 2], [4, 1]],	[[3, 3], [3, 3]]))
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))