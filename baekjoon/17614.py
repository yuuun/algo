n = int(input())
cnt = 0
for i in range(1, n + 1):
    i = str(i)
    cnt += i.count('3') + i.count('6') + i.count('9')
print(cnt)