score = [[i * 2 for i in range(21)],
        [10, 13, 16, 19], #10분기
        [20, 22, 24], #20분기
        [30, 28, 27, 26], #30분기
        [25, 30, 35, 40]] #중복
dices = list(map(int, input().split()))
dice_loc = [[0, 0] for _ in range(4)]
s, a, b, = 0, 0, 0
def check_duplicate(x, y, i):
    global a, b, s
    a = dice_loc[i][0]
    b = dice_loc[i][1]
    s = score[dice_loc[i][0]][dice_loc[i][1]]
    # score[dice_loc[0][0]][dice_loc[0][1]] == score[dice_loc[2][0]][dice_loc[2][1]] == 40
    for j in range(4):
        if i != j:
            if dice_loc[j] == [x, y]:
                return False
            # if s == score[dice_loc[j][0]][dice_loc[j][1]] == 40:
            #     return False
    return True

ans = set()
# ans = []
def dfs(cnt, idx):
    if idx == len(dices):
        ans.add(cnt)
        # ans.append(cnt)
        return
    
    for i, value in enumerate(dice_loc):
        x, y = value
        if (x, y) == (-1, -1):
            continue
        
        ty = y + dices[idx]
        if x == 0:
            if ty % 5 == 0:
                tx = ty // 5
                if ty == len(score[0]) - 1:
                    if check_duplicate(4, 3, i):
                        dice_loc[i] = [4, 3]
                        dfs(cnt + score[0][-1], idx + 1)
                        dice_loc[i] = [x, y]
                else:
                    if check_duplicate(tx, 0, i):
                        dice_loc[i] = [tx, 0]
                        dfs(cnt + score[tx][0], idx + 1)
                        dice_loc[i] = [x, y]
                    
            elif ty >= len(score[0]):
                dice_loc[i] = [-1, -1]
                dfs(cnt, idx + 1)
                dice_loc[i] = [x, y]
            
            else:
                if check_duplicate(x, ty, i):
                    dice_loc[i] = [x, ty]
                    dfs(cnt + score[x][ty], idx + 1)
                    dice_loc[i] = [x, y]
        elif x == 4:
            if len(score[x]) <= ty:
                dice_loc[i] = [-1, -1]
                dfs(cnt, idx + 1)
                dice_loc[i] = [x, y]
            else:
                if check_duplicate(x, ty, i):
                    dice_loc[i] = [x, ty]
                    dfs(cnt + score[x][ty], idx + 1)
                    dice_loc[i] = [x, y]
        else:
            if len(score[x]) <= ty:
                ty = ty - len(score[x])
                if ty >= len(score[4]):
                    dice_loc[i] = [-1, -1]
                    dfs(cnt, idx + 1)
                    dice_loc[i] = [x, y]
                elif check_duplicate(4, ty, i):
                    dice_loc[i] = [4, ty]
                    dfs(cnt + score[4][ty], idx + 1)
                    dice_loc[i] = [x, y]
            else:
                if check_duplicate(x, ty, i):
                    dice_loc[i] = [x, ty]
                    dfs(cnt + score[x][ty], idx + 1)
                    dice_loc[i] = [x, y]


dfs(0, 0)
print(ans)
print(max(ans))