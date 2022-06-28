n = int(input())

cnt = 0
for c in range(2, n, 2):
    tot = 0
    if n - c > 2:
        for a in range(1, n - c):
            for b in range(a + 2, n - c):
                if a + b + c == n: 
                    cnt += 1
    else:
        break
print(cnt)