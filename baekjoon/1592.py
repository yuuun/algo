N, M, L = map(int, input().split())

cnt_list = [0 for _ in range(N)]
cnt_list[0] = 1
cur = 0
def re_cur(c):
    if c >= N:
        c -= N
    elif c < 0:
        c += N
    return c
cnt = 0
while max(cnt_list) < M:
    
    if cnt_list[cur] % 2 == 0:
        cur -= L
        cur = re_cur(cur)
    else:
        cur += L
        cur = re_cur(cur)
    cnt += 1 
    cnt_list[cur] += 1
print(cnt)