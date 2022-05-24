def solution(arr1, arr2):
    answer = []
    for x, y in zip(arr1, arr2):
        tmp = []
        for i, j in zip(x, y):
            tmp.append(i + j)
        answer.append(tmp)
    return answer