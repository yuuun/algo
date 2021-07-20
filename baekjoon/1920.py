n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
bb = list(map(int, input().split()))

def binary_search(b, start, end):
    if start > end:
        return 0
    m = (start + end) // 2
    if b == a[m]:
        return 1
    elif b < a[m]:
        return binary_search(b, start, m - 1)
    else:
        return binary_search(b, m + 1, end)
        
for b in bb:
    print(binary_search(b, 0, n - 1))