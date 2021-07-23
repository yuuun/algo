n, a = int(input()), sorted(list(map(int, input().split())))
m, b = int(input()), list(map(int, input().split()))

def binary_search(bb, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if bb == a[mid]:
        return 1
    if bb < a[mid]:
        return binary_search(bb, start, mid - 1)
    if bb > a[mid]:
        return binary_search(bb, mid + 1, end)

for bb in b:
    print(binary_search(bb, 0, n - 1), end=' ')