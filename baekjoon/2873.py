#greedy algorithm
r, c = map(int, input().split())
li = []
for _ in range(r):
    li.append(list(map(int, input().split())))

if r % 2 == 1:
    print(('R' * (c - 1) + 'D' + 'L' * (c - 1) + 'D') * (r // 2) + 'R' * (c - 1))
elif c % 2 == 1:
    print(('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (c // 2) + 'D' * (r - 1))
else:
    r_min, c_min = 0, 1
    for _r in range(r):
        for _c in range(c):
            if (_r + _c) % 2 == 1:
                if li[r_min][c_min] > li[_r][_c]:
                    r_min = _r
                    c_min = _c
                    
    ans = ''
    ans += ('D' * (r - 1) + 'R' + 'U' * (r - 1) + 'R') * (c_min // 2)
    
    ans += ('RDLD') * (r_min // 2)
    if c_min % 2 == 0:
        ans += 'RD'
    else:
        ans += 'DR'
    
    ans += ('DLDR') * ((r - r_min - 1) // 2)
    
    ans += ('R' + 'U' * (r - 1) + 'R' + 'D' * (r-1)) * ((c - c_min - 1) // 2)
    
    print(ans)