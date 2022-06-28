n = int(input())
arr = []
for i in range(1, n + 1):
    cur = [n, i]
    while True:
        next_num = cur[-2] - cur[-1]
        if next_num < 0:
            break
        cur.append(next_num)
    
    if len(arr) < len(cur):
        arr = cur

print(len(arr))
print(' '.join(map(str, arr)))