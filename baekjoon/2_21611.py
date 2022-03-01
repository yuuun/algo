from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
dire = [list(map(int, input().split())) for _ in range(m)]
dxy = [[0, -1], [1, 0], [0, 1], [-1, 0]] # 서 남 동 북

n_2 = n // 2
maps[n_2][n_2] = 5

# 각 인덱스에 해당하는 지도의 좌표 구하기
def get_index():
    sx, sy = n_2, n_2
    size_map = n ** 2
    cnt = 1
    idx = 1
    index_dic = {}
    while size_map > idx:
        for i in range(4):
            t = 0
            while t < cnt and size_map > idx:
                sx += dxy[i][0]
                sy += dxy[i][1]
                index_dic[idx] = [sx, sy]
                t += 1
                idx += 1
            if i in [1, 3]:
                cnt += 1
    return index_dic

index_dic = get_index()

# 방향의 dis만큼 의미없는 값인 5로 수정
def do_blizard(dir, dis):
    dir_dic = [None, 3, 1, 0, 2]
    dir = dir_dic[dir]
    sx, sy = n_2, n_2
    for _ in range(dis):
        sx += dxy[dir][0]
        sy += dxy[dir][1]
        if 0 <= sx < n and 0 <= sy < n:
            maps[sx][sy] = 5
        else:
            break

# 연속된 숫자일 경우 제거해주기
def squeeze_queue(q):
    global ans
    new_q = deque()
    cur, cnt = q[0], 0
    while q:
        next = q.popleft()
        if cur == next:
            cnt += 1
        else:
            if cnt < 4:
                new_q.extend([cur] * cnt)
            else:
                ans += cur * cnt
            cnt = 1
            cur = next
    if cnt < 4:
        new_q.extend([cur] * cnt)
    else:
        ans += cur * cnt
    return new_q

# 연속된 숫자 누적 합을 [구슬의 색, 구슬의 갯수]로 반환
def count_queue(q):
    cnt_q = deque()
    cur, cnt = q[0], 0
    while q:
        next = q.popleft()
        if cur == next:
            cnt += 1
        else:
            cnt_q.append([cur, cnt])
            cnt = 1
            cur = next
    
    cnt_q.append([cur, cnt])
    return cnt_q

def make_queue():
    global ans
    cur = maps[n_2][n_2 - 1]
    q = deque() 
    for _, values in index_dic.items():
        sx, sy = values
        marble = maps[sx][sy]
        if marble == 0:
            break
        if marble == 5:
            continue
        q.append(marble)
    
    len_q = len(q)
    # 줄이다 보면 q에 남아 있는게 없을 경우 존재
    while q:
        q = squeeze_queue(q)
        if len(q) == len_q:
            break
        else:
            len_q = len(q)
    if q:
        cnt_q = count_queue(q)
        return cnt_q
    return False

def make_maps(q):
    new_maps = [[0] * n for _ in range(n)]
    for idx, values in index_dic.items():
        sx, sy = values
        if q:
            if idx % 2 == 0:
                cur, cnt = q.popleft()
                new_maps[sx][sy] = cur
            else:
                new_maps[sx][sy] = q[0][1]
        else:
            break
    return new_maps

ans = 0
for dir, dis in dire:
    do_blizard(dir, dis)
    q = make_queue()
    if q:
        maps = make_maps(q)
    else:
        break

print(ans)