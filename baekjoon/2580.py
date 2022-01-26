from collections import deque
sudoku = []
q = deque()
for i in range(9):
    tmp = list(map(int, input().split()))
    for j, t in enumerate(tmp):
        if t == 0:
            q.append([i, j])
    sudoku.append(tmp)

nums =  set(list(range(1, 10)))
def getNum(cand):
    tmp = set(cand)
    if len(tmp) == 9:
        return list(nums.difference(cand))[0]
    return 0

def getRow(x):
    return sudoku[x]

def getcol(y):
    cols = []
    for i in range(9):
        cols.append(sudoku[i][y])
    return cols

def getbox(x, y):
    cols = []
    x //= 3
    y //= 3
    x *= 3
    y *= 3

    for i in range(x, x + 3):
        for j in range(y, y + 3):
            cols.append(sudoku[i][j])
    return cols


while q:
    x, y = q.popleft()
    r = getNum(getRow(x))
    if r != 0:
        sudoku[x][y] = r
    else:
        c = getNum(getcol(y))
        if c != 0:
            sudoku[x][y] = c
        else:
            b = getNum(getbox(x, y))
            if b != 0:
                sudoku[x][y] = b
    
    if sudoku[x][y] == 0:
        q.append([x, y])

for su in sudoku:
    print(' '.join(map(str, su)))