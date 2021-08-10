T = int(input())
n = int(input())
m1 = sorted(list(map(int, input().split())))
m = int(input())
m2 = list(map(int, input().split()))

def binary_search(seq, val, start, end):
    while start <= end:
        mid = (start + end) // 2
        if seq[mid] == val:
            return 1
        elif seq[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for tmp in m2:
    print(binary_search(m1, tmp, 0, n - 1))