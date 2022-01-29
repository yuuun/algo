a, b, c = map(int, input().split())
s_1, s_2 = b - a, c - b
if s_1 == s_2 == 1:
    print(0)
elif s_1 > s_2:
    print(s_1 - 1)
else:
    print(s_2 - 1)
