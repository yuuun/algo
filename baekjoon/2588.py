x = int(input())
y = input()
ans = 0
for idx, i in enumerate(reversed(y)):
    tmp = x * int(i)
    print(tmp)
    ans += tmp * (10 ** (idx))
print(ans)