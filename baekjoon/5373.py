# 위, 아래, 앞, 뒤, 왼, 오른
dice_order = ['w', 'y', 'r', 'o', 'g', 'b']
def rotate90(arr):
    return [list(elem) for elem in zip(*arr[::-1])]

def rotate_R(dire):
    if dire == '-':
        k = 3
    else:
        k = 1

    for _ in range(k):
        dice[5] = rotate90(dice[5])
        dice[0][0][2], dice[2][0][2], dice[1][0][2], dice[3][2][0] = dice[2][0][2], dice[1][0][2], dice[3][2][0], dice[0][0][2]
        dice[0][1][2], dice[2][1][2], dice[1][1][2], dice[3][1][0] = dice[2][1][2], dice[1][1][2], dice[3][1][0], dice[0][1][2]
        dice[0][2][2], dice[2][2][2], dice[1][2][2], dice[3][0][0] = dice[2][2][2], dice[1][2][2], dice[3][0][0], dice[0][2][2]

def rotate_L(dire):
    if dire == '-':
        k = 3
    else:
        k = 1
    
    for _ in range(k):
        dice[4] = rotate90(dice[4])
        dice[0][0][0], dice[3][2][2], dice[1][0][0], dice[2][0][0] = dice[3][2][2], dice[1][0][0], dice[2][0][0], dice[0][0][0]
        dice[0][1][0], dice[3][1][2], dice[1][1][0], dice[2][1][0] = dice[3][1][2], dice[1][1][0], dice[2][1][0], dice[0][1][0]
        dice[0][2][0], dice[3][0][2], dice[1][2][0], dice[2][2][0] = dice[3][0][2], dice[1][2][0], dice[2][2][0], dice[0][2][0]

def rotate_U(dire):
    if dire == '-':
        k = 3
    else:
        k = 1
    
    for _ in range(k):
        dice[0] = rotate90(dice[0])
        for i in range(3):
            dice[4][0][i], dice[2][0][i], dice[5][0][i], dice[3][0][i] = dice[2][0][i], dice[5][0][i], dice[3][0][i], dice[4][0][i]

def rotate_D(dire):
    if dire == '-':
        k = 3
    else:
        k = 1
    
    for _ in range(k):
        dice[1] = rotate90(dice[1])
        for i in range(3):
            dice[4][2][i], dice[3][2][i], dice[5][2][i], dice[2][2][i] = dice[3][2][i], dice[5][2][i], dice[2][2][i], dice[4][2][i]

def rotate_F(dire):
    if dire == '-':
        k = 3
    else:
        k = 1
    
    for _ in range(k):
        dice[2] = rotate90(dice[2])
        dice[0][2][0], dice[4][2][2], dice[1][0][2], dice[5][0][0] = dice[4][2][2], dice[1][0][2], dice[5][0][0], dice[0][2][0]
        dice[0][2][1], dice[4][1][2], dice[1][0][1], dice[5][1][0] = dice[4][1][2], dice[1][0][1], dice[5][1][0], dice[0][2][1]
        dice[0][2][2], dice[4][0][2], dice[1][0][0], dice[5][2][0] = dice[4][0][2], dice[1][0][0], dice[5][2][0], dice[0][2][2]

def rotate_B(dire):
    if dire == '-':
        k = 3
    else:
        k = 1
    
    for _ in range(k):
        dice[3] = rotate90(dice[3])
        dice[0][0][0], dice[5][0][2], dice[1][2][2], dice[4][2][0] = dice[5][0][2], dice[1][2][2], dice[4][2][0], dice[0][0][0]
        dice[0][0][1], dice[5][1][2], dice[1][2][1], dice[4][1][0] = dice[5][1][2], dice[1][2][1], dice[4][1][0], dice[0][0][1]
        dice[0][0][2], dice[5][2][2], dice[1][2][0], dice[4][0][0] = dice[5][2][2], dice[1][2][0], dice[4][0][0], dice[0][0][2]


for _ in range(int(input())):
    # 위, 아래, 앞, 뒤, 왼, 오른
    dice = [[[d] * 3 for _ in range(3)] for d in dice_order]
    t = int(input())
    order = list(input().split())
    for cur in order:
        if cur[0] == 'R':
            rotate_R(cur[1])
        elif cur[0] == 'L':
            rotate_L(cur[1])
        elif cur[0] == 'U':
            rotate_U(cur[1])
        elif cur[0] == 'D':
            rotate_D(cur[1])
        elif cur[0] == 'F':
            rotate_F(cur[1])
        else:
            rotate_B(cur[1])
    
    for di in dice[0]:
        print(''.join(di))