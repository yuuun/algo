#TBD
n, max_val = map(int, input().split())

if n == 0:
    print(max_val, 0)
else:
    def get_direc(cur_dir, str_dir):
        if str_dir == 'right':
            if cur_dir[0] == 0:
                cur_dir = [cur_dir[1], 0]
            else:
                cur_dir = [0, -cur_dir[0]]
        elif str_dir == 'left':
            if cur_dir[0] == 0:
                cur_dir = [-cur_dir[1], 0]
            else:
                cur_dir = [0, cur_dir[0]]
        return cur_dir

        return cur, cur_dir
    def move(cur, cur_dir, mov):
        return [cur_dir[0] * mov + cur[0], cur_dir[1] * mov + cur[1]]

    cur = [0, 0]
    cur_dir = [1, 0]
    
    cur_time = 0
    dir_info = []
    for _ in range(n):
        num, str_dir = map(str, input().split())
        dir_info.append([int(num), str_dir])
    dir_info.append([max_val])
    time_list = []
    for idx in range(0, n):
        time_list.append(dir_info[idx + 1][0] - dir_info[idx][0])
    
    cur = move(cur, cur_dir, cur_dir[0])
    for idx, val in enumerate(time_list):
        cur_dir = get_direc(cur_dir, dir_info[idx][1])
        
        cur = move(cur, cur_dir, time_list[idx])
    print(' '.join(map(str, cur)))