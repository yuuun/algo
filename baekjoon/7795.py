T = int(input())

def binary_search(seq, target):
    start, end = 0, len(seq) - 1
    res = -1
    while start <= end:
        mid = (start + end) // 2
        if seq[mid] < target:
            res = mid
            start = mid + 1
        else:
            end = end - 1
    return res
    
for _ in range(T):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for a in A:
        cnt += binary_search(B, a) + 1
    print(cnt)