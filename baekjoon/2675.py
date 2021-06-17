n = int(input())
for _ in range(n):
    rep, string = input().split()
    rep = int(rep)
    ans = ''
    for st in string:
        ans += st * rep
    print(ans)