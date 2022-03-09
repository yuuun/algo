n, k = map(int, input().split())
fish = list(map(int, input().split()))

def fill_fish():
    min_fish = min(fish)
    for i in range(n):
        if fish[i] == min_fish:
            fish[i] += 1

def rotate_fish(arr):
    return [list(elem) for elem in zip(*arr[::-1])]

def down_fish(arr, r, c):
    new_fish = []
    for i in range(c):
        for j in range(r - 1, -1, -1):
            new_fish.append(arr[j][i])
    return new_fish

dxy = [[0, 1], [1, 0]]
def do_first():
    left_fish = [[fish[0]], [fish[1]]]
    right_fish = fish[2:]
    cnt = 2
    i = 0
    while True:
        left_fish = rotate_fish(left_fish) + [right_fish[:cnt]]
        right_fish = right_fish[cnt:]
        if i % 2 == 1:
            cnt += 1
        if len(right_fish) < cnt:
            break
        
        i += 1
    r, c = len(left_fish), len(left_fish[0])
    
    left_cnt = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if nx < r and ny < c:
                    sub = abs(left_fish[x][y] - left_fish[nx][ny]) // 5
                    if sub > 0:
                        if left_fish[x][y] > left_fish[nx][ny]:
                            left_cnt[x][y] -= sub
                            left_cnt[nx][ny] += sub
                        else:
                            left_cnt[x][y] += sub
                            left_cnt[nx][ny] -= sub
    
    if len(right_fish) == 0:
        for i in range(r):
            for j in range(c):
                left_fish[i][j] += left_cnt[i][j]
        return down_fish(left_fish, r, c)
        
    right_cnt = [0] * len(right_fish)
    sub = abs(right_fish[0] - left_fish[-1][-1]) // 5
    if sub > 0:
        if right_fish[0] > left_fish[-1][-1]:
            left_cnt[-1][-1] += sub
            right_cnt[0] -= sub
        else:
            left_cnt[-1][-1] -= sub
            right_cnt[0] += sub

    for i in range(len(right_fish) - 1):
        sub = abs(right_fish[i] - right_fish[i + 1]) // 5
        if sub > 0:
            if right_fish[i] > right_fish[i + 1]:
                right_cnt[i] -= sub
                right_cnt[i + 1] += sub
            else:
                right_cnt[i] += sub
                right_cnt[i + 1] -= sub

    for i in range(r):
        for j in range(c):
            left_fish[i][j] += left_cnt[i][j]
    for i in range(len(right_fish)):
        right_fish[i] += right_cnt[i]
        
    # 어항 내려놓기
    new_fish = down_fish(left_fish, r, c)
    new_fish = new_fish + right_fish
    return new_fish

def do_second():
    new_fish = [fish[:n//2][::-1], fish[n//2:]]
    left_fish = [new_fish[i][:n // 4] for i in range(len(new_fish))]
    left_fish = rotate_fish(rotate_fish(left_fish))
    right_fish = [new_fish[i][n//4:] for i in range(len(new_fish))]
    new_fish = left_fish + right_fish
    r, c = len(new_fish), len(new_fish[0])
    cnt_list = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if nx < r and ny < c:
                    sub = abs(new_fish[x][y] - new_fish[nx][ny]) // 5
                    if sub > 0:
                        if new_fish[x][y] > new_fish[nx][ny]:
                            cnt_list[x][y] -= sub
                            cnt_list[nx][ny] += sub
                        else:
                            cnt_list[x][y] += sub
                            cnt_list[nx][ny] -= sub

    for i in range(r):
        for j in range(c):
            new_fish[i][j] += cnt_list[i][j]
    return down_fish(new_fish, r, c)

def check_final():
    if max(fish) - min(fish) > k:
        return False
    return True

ans = 1
while True: 
    fill_fish() # 최소값 가지는 어항에 물고기 추가
    fish = do_first() # 달팽이 모양으로 계속 쌓는 과정
    fish = do_second() 
    
    if check_final():
        break
    ans += 1
print(ans)