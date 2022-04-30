M, N = map(int, input().split())

top, bottom, left, right = 0, M, 0, N

if M <= N:
    turn = 2 * (M - 1)
else:
    turn = 2 * N - 1

mok, nameoji = divmod(turn, 4)

if nameoji == 0:
    top += mok; bottom -= mok; right -= mok; left += mok
    r = bottom; c = right 
elif nameoji == 1:
    top = top + mok + 1; bottom -= mok; right -= mok; left += mok
    r = bottom; c = right 
elif nameoji == 2:
    top = top + mok + 1; bottom -= mok; right = right - mok -1; left += mok
    r = bottom; c = left + 1 
else:
    top = top + mok + 1; bottom = bottom - mok -1
    right = right - mok -1; left += mok
    r = top + 1; c = right

print(turn)
print(r, c)