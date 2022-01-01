#TBD 
dir = [[0, 0], [-1, 0], [-1, -1], [0, -1], [1, -1], 
        [1, 0], [1, 1], [0, 1], [-1, 1]]

loc = []
for _ in range(4):
    loc_tmp = []
    tmp = list(map(int, input().split()))
    for i in range(4):
        loc_tmp.append([tmp[2 * i], tmp[2 * i + 1]])
    loc.append(loc_tmp)
print(loc)