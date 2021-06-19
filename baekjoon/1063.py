k, s, n = map(str, input().split())
mov_dict = {'R': [0, 1], 'L': [0, -1], 'B': [1, 0], 'T': [-1, 0],
            'RT': [-1, 1], 'LT': [-1, -1], 'RB': [1, 1], 'LB': [1, -1]}
row = ['8', '7', '6', '5', '4', '3', '2', '1']
col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
cur_king = [row.index(k[1]), col.index(k[0])]
cur_stone = [row.index(s[1]), col.index(s[0])]

for _ in range(int(n)):
    mov = mov_dict[input()]
    cur_row = cur_king[0] + mov[0]
    cur_col = cur_king[1] + mov[1]
    if 0 <= cur_row < 8 and 0 <= cur_col < 8:
        cur_s_row = cur_stone[0] + mov[0]
        cur_s_col = cur_stone[1] + mov[1]
        if [cur_row, cur_col] != cur_stone:
            cur_king = [cur_row, cur_col]
        elif 0 <= cur_s_row < 8 and 0 <= cur_s_col < 8:
            cur_stone = [cur_s_row, cur_s_col]
            cur_king = [cur_row, cur_col]

print(col[cur_king[1]] + row[cur_king[0]])
print(col[cur_stone[1]] + row[cur_stone[0]])