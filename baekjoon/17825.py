import sys

input = sys.stdin.readline
score = [[i * 2 for i in range(21)],
         [10, 13, 16, 19],  # 10분기
         [20, 22, 24],  # 20분기
         [30, 28, 27, 26],  # 30분기
         [25, 30, 35, 40]]  # 중복
dices = list(map(int, input().split()))
dice_loc = [[0, 0] for _ in range(4)]
s, a, b, = 0, 0, 0


# 말이 이동한 곳에 이미 말이 있는지 체크
def check_duplicate(x, y, i):
    for j in range(4):
        if i != j:
            if dice_loc[j] == [x, y]:
                return False
    return True


max_val = 0

def dfs(cnt, idx):
    global max_val
    if idx == len(dices):
        max_val = max(max_val, cnt)
        return

    for i, value in enumerate(dice_loc):
        x, y = value
        if (x, y) == (-1, -1):
            continue

        ty = y + dices[idx]
        if x == 0:
            # 마지막 위치일 경우
            if ty == 20:
                if check_duplicate(4, 3, i):
                    dice_loc[i] = [4, 3]
                    dfs(cnt + score[0][-1], idx + 1)
                    dice_loc[i] = [x, y]

            # 갈림길
            elif ty % 5 == 0:
                tx = ty // 5
                if check_duplicate(tx, 0, i):
                    dice_loc[i] = [tx, 0]
                    dfs(cnt + score[tx][0], idx + 1)
                    dice_loc[i] = [x, y]

            elif ty > 20:
                dice_loc[i] = [-1, -1]
                dfs(cnt, idx + 1)
                dice_loc[i] = [x, y]

            else:
                if check_duplicate(x, ty, i):
                    dice_loc[i] = [x, ty]
                    dfs(cnt + score[x][ty], idx + 1)
                    dice_loc[i] = [x, y]
        # 마지막 공통인 부분: 25, 30, 35, 40일 떄
        elif x == 4:
            if 3 < ty:
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
print(max_val)