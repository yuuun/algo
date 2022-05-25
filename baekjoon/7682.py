def change_maps(maps):
    return [list(maps[:3]), list(maps[3:6]), list(maps[6:])]

def check_bingo(maps, string):
    for i in range(3):
        if maps[i][0] == string and maps[i][1] == string and maps[i][2] == string:
            return True
    for j in range(3):
        if maps[0][j] == string and maps[1][j] == string and maps[2][j] == string:
            return True
    if maps[1][1] == string:
        if maps[0][0] == string and maps[2][2] == string:
            return True
        if maps[0][2] == string and maps[2][0] == string:
            return True
    return False

while True:
    maps = input()
    if maps == 'end':
        break
    n_o = maps.count('O')
    n_x = maps.count('X')
    if n_o != n_x and n_o + 1 != n_x:
        print('invalid')
        continue
    maps = change_maps(maps)
    
    if n_o == n_x:
        is_o = check_bingo(maps, 'O')
        is_x = check_bingo(maps, 'X')
        if is_x:
            print('invalid')
        elif is_o:
            print('valid')
        elif n_o + n_x < 8:
            print('invalid')

    elif n_o + 1 == n_x:
        is_o = check_bingo(maps, 'O')
        is_x = check_bingo(maps, 'X')
        if is_o:
            print('invalid')
            continue
        elif is_x:
            print('valid')
            continue
        if n_o + n_x < 9:
            print('invalid')
        else:
            print('valid')
    
    else:
        print('invalid')
        continue