n = int(input())
ws = list(map(int, input().split()))
max_val = 0
def sol(t, arr):
    global max_val
    if len(arr) == 2:
        max_val = max(t, max_val)
        return
    
    for i in range(1, len(arr) - 1):
        mid = arr[i - 1] * arr[i + 1]
        sol(t + mid, arr[:i] + arr[i + 1:])

sol(0, ws)
print(max_val)