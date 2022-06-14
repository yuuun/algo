import sys
sys.setrecursionlimit(10**6)

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

def sol(first, end):
    if first > end:
        return
    mid = end + 1
    for i in range(first + 1, end + 1):
        if arr[first] < arr[i]:
            mid = i
            break
    sol(first + 1, mid - 1)
    sol(mid, end)
    print(arr[first])

sol(0, len(arr) - 1)