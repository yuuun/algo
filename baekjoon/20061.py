
blue = [[False] * 6 for _ in range(4)] # 비어있을 경우: False, 차 있을 경우: True
green = [[False] * 4 for _ in range(6)]
n = int(input())
s = 0
def check_blue():
    global s
    for j in range(2, 6):
        cnt = 0
        for i in range(4):
            if blue[i][j]:
                cnt += 1
        if cnt == 4:
            remove_blue(j)
            s += 1

def remove_blue(k):
    for j in range(k, 0, -1):
        for i in range(4):
            blue[i][j] = blue[i][j - 1]

    for i in range(4):
        blue[i][0] = False

def move_blue():
    global t, x, y, s, blue
    if t == 3:
        ny = -1
        for j in range(6):
            flag = True
            for i in [x, x + 1]:
                if blue[i][j]:
                    flag = False
                    break
            if not flag:
                break
            ny = j
        blue[x][ny] = True
        blue[x + 1][ny] = True

        if ny == 1:
            remove_blue(5)
        check_blue()

    else:
        ny = -1
        flag = True
        for j in range(2, 6):
            if blue[x][j]:
                flag = False
                break
        if flag:
            ny = 5
        else:
            ny = j - 1

        blue[x][ny] = True
        if t == 2:
            blue[x][ny - 1] = True
        check_blue()
        if blue[x][1]:
            remove_blue(5)
        if blue[x][1]:
            remove_blue(5)

def check_green():
    global s
    for i in range(2, 6):
        cnt = 0
        for j in range(4):
            if green[i][j]:
                cnt += 1
        if cnt == 4:
            remove_green(i)
            s += 1

def remove_green(k):
    global green
    for i in range(k, 0, -1):
        for j in range(4):
            green[i][j] = green[i - 1][j]

    for j in range(4):
        green[0][j] = False

def move_green():
    global t, x, y, s, green
    if t == 2:
        nx = -1
        for i in range(6):
            flag = True
            for j in [y, y + 1]:
                if green[i][j]:
                    flag = False
                    break
            if not flag:
                break
            nx = i
        green[nx][y] = True
        green[nx][y + 1] = True

        if nx == 1:
            remove_green(5)
        check_green()

    else:
        nx = -1
        flag = True
        for i in range(2, 6):
            if green[i][y]:
                flag = False
                break
        if flag:
            nx = 5
        else:
            nx = i - 1

        green[nx][y] = True
        if t == 3:
            green[nx - 1][y] = True
        check_green()
        if green[1][y]:
            remove_green(5)
        if green[1][y]:
            remove_green(5)

for _ in range(n):
    t, x, y = map(int, input().split())
    move_blue()
    move_green()
print(s)

n_block = 0
for i in range(4):
    for j in range(6):
        if blue[i][j]:
            n_block += 1
for i in range(6):
    for j in range(4):
        if green[i][j]:
            n_block += 1
print(n_block)