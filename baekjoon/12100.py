# 2048  # 실패
from copy import deepcopy

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

def turn_left():
    global maps
    for i in range(n):
        tmp = [num for num in maps[i] if num != 0]
        if tmp != []:
            t = tmp[0]
            isTrue = False
            for j in range(1, len(tmp)):
                if t == tmp[j]:
                    tmp[j - 1] *= 2
                    isTrue = True
                    break
                else:
                    t = tmp[j]
            if isTrue:
                tmp = tmp[:j] + tmp[j + 1:]
            tmp = tmp + [0] * (n - len(tmp))
            maps[i] = tmp
    return maps

def turn_right():
    global maps
    for i in range(n):
        tmp = [num for num in maps[i] if num != 0]
        if tmp != []:
            t = tmp[-1]
            isTrue = False
            for j in range(len(tmp) - 2, -1, -1):
                if t == tmp[j]:
                    tmp[j + 1] *= 2
                    isTrue = True
                    break
                else:
                    t = tmp[j]
            if isTrue:
                tmp = tmp[:j] + tmp[j + 1:]
            tmp = [0] * (n - len(tmp)) + tmp
            maps[i] = tmp
    return maps

def sum_map(dir):
    global maps
    if dir == 0:        # 왼쪽으로 이동
        turn_left()

    elif dir == 1:  # 오른쪽으로 이동
        turn_right()
    
    elif dir == 2: #위로 이동
        # 90도 회전
        maps = [list(tmp) for tmp in zip(*maps[::-1])]
        maps = turn_right()
        maps = [list(tmp) for tmp in zip(*maps)][::-1]
    
    else:       # 아래로 이동
        maps = [list(tmp) for tmp in zip(*maps[::-1])]
        maps = turn_left()
        maps = [list(tmp) for tmp in zip(*maps)][::-1]
        

def get_max():
    max_val = 0
    for info in maps:
        max_val = max(max_val, max(info))
    return max_val

ans = []
def dfs(cnt):
    global maps
    if cnt == 5:
        ans.append(get_max())
        return

    tmp_maps = deepcopy(maps)
    for i in range(4):
        sum_map(i)
        dfs(cnt + 1)
        maps = deepcopy(tmp_maps)

dfs(0)
print(max(ans))

# maps = sum_map(maps, 2)
# maps = sum_map(maps, 1)
# max_val = get_max(maps)
# print('end')