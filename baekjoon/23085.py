def combinations(arr, r):
    for i in range(len(arr)):
        if i == 1:
            yield [arr[i]]
        else:
            for j in combinations(arr[i + 1:], r - 1):
                yield [arr[i]] + j

n, k = map(int, input().split())
lis = [i for i in range(n)]

