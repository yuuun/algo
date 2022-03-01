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

# 나중에 안 될 경우 확인
def double_check(q):
    new_q = deque()
    while q:
        cur, cnt = q.popleft()
        while new_q and new_q[-1][0] == cur:
            new_cur, new_cnt = new_q.pop()
            if new_cnt + cnt < 4:
                new_q.append([new_cur, new_cnt + cnt])
        else:
            new_q.append([cur, cnt])
    return new_q

def make_queue():
    global ans
    cur = maps[n_2][n_2 - 1]
    q = deque() # 구슬의 idx와 해당 구슬의 개수 추가하기
    tmp_list = []
    for _, values in index_dic.items():
        sx, sy = values
        marble = maps[sx][sy]
        if marble == 0:
            break
        if marble == 5:
            continue
        if cur == marble:
            tmp_list.append(marble)
        else:
            if 0 < len(tmp_list) < 4:
                if not q:
                    q.append([cur, len(tmp_list)])
                else:
                    if q[-1][0] == cur:
                        idx, cnt = q.pop()
                        cnt += len(tmp_list)
                        if cnt < 4:
                            q.append([cur, cnt])
                        else:
                            ans += cur * cnt
                    else:
                        q.append([cur, len(tmp_list)])
            else:
                ans += cur * len(tmp_list)
                
            tmp_list = [marble]
            cur = marble

    q.append([cur, len(tmp_list)])
    q = double_check(q)
    return q

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
    maps = make_maps(q)
print(ans)
ssums = 0
for i in maps:
    ssums += sum(i)