n = int(input())
cnt = 0
for i in range(1, n):
    ans = i
    tmp = str(i)
    for j in tmp:
        ans += int(j)
    if ans == n:
        cnt = i
        break
print(cnt)