r, c = map(int, input().split())

lis = [['.' for _ in range(c)] for _ in range(r)]
res = [['.' for _ in range(c)] for _ in range(r)]
for idx in range(r):
    val = input()
    for i, v in enumerate(val):
        if v == 'X':
            lis[idx][i] = 'X'
            res[idx][i] = 'X'

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#섬이 가라앉는지 확인하기 위함
for i1, li in enumerate(lis):
    for i2, l in enumerate(li):
        cnt = 0
        if l == 'X':
            for x, y in zip(dx, dy):
                tmp1 = i1 + x
                tmp2 = i2 + y
                if 0 <= tmp1 < r and 0 <= tmp2 < c:
                    if lis[tmp1][tmp2] == '.':
                        cnt += 1
                else:
                    cnt += 1
            if cnt > 2:
                res[i1][i2] = '.'

#섬에 해당하는 부분만 프린트하기 
r_s, r_e = 0, 0
for idx, val in enumerate(res):
    if 'X' in val:
        r_s = idx
        break

for idx, val in enumerate(res[::-1]):
    if 'X' in val:
        r_e = r - idx
        break

result = []
for idx in range(c):
    for i in range(r_s, r_e):
        if res[i][idx] == 'X':
            result.append(idx)

for idx in range(r_s, r_e):
    print(''.join(res[idx][result[0] : result[-1] + 1]))