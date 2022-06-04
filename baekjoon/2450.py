from collections import Counter
n = int(input())
arr = list(map(int, input().split()))

cnt_list = Counter(arr)

def permutation(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for j in permutation(arr[:i] + arr[i + 1:], r - 1):
                yield [arr[i]] + j

ans = 1e10
def calculate_count(match):
    i, j, k = match
    ji, ki = 0, 0
    jk, kj = 0, 0
    for a in range(cnt_list[i]):
        if arr[a] == j:
            ji += 1
        if arr[a] == k:
            ki += 1
    for a in range(cnt_list[i], cnt_list[i] + cnt_list[j]):
        if arr[a] == k:
            kj += 1
    
    for a in range(cnt_list[i] + cnt_list[j], len(arr)):
        if arr[a] == j:
            jk += 1
    
    return ji + ki + max(jk, kj)


for match in permutation([1, 2, 3], 3):
    ans = min(ans, calculate_count(match))
print(ans)