sl, sr = map(str, input().split())
li = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
        ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
string = input()

def get_idx(s):
    for r, l in enumerate(li):
        if s in l:
            c = l.index(s)
            tmp = 3 if r == 2 else 4
            if c > tmp:
                return r, c, True
            else: 
                return r, c, False

r_l, c_l, _ = get_idx(sl)
r_r, c_r, _ = get_idx(sr)
ans = 0            
for s in string:
    r2, c2, isRight = get_idx(s)
    print(r2, c2, r_l, c_l, r_r, c_r, isRight)
    if isRight:
        ans += abs(r_r - r2) + abs(c_r - c2)
        r_r, c_r = r2, c2
    else:
        ans += abs(r_l - r2) + abs(c_l - c2)
        r_l, c_l = r2, c2

print(ans + len(string))