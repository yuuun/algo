n = int(input())
n1 = n + 1

maps = [None]
total_sum = 0
for  _ in range(n):
    tmp = list(map(int, input().split()))
    maps.append([0] + tmp)
    total_sum += sum(tmp)

def solution(x, y, d1, d2):
    cnt_list = [0] * 5 # 각 구역별 인구 수
    # 1
    for i in range(1, x):
        cnt_list[1] += sum(maps[i][1:y + 1])
    for d in range(d1):
        cnt_list[1] += sum(maps[x + d][1:y - d])
    
    # 2
    for i in range(1, x):
        cnt_list[2] += sum(maps[i][y + 1:])
    for d in range(d2 + 1):
        cnt_list[2] += sum(maps[x + d][y + d + 1:])
    
    # 3
    for d in range(d2 + 1):
        cnt_list[3] += sum(maps[x + d1 + d][1:y - d1 + d])
    for i in range(x + d1 + d2 + 1, n1):
        cnt_list[3] += sum(maps[i][1:y - d1 + d2])
    
    # 4
    for d in range(1, d1 + 1):
        cnt_list[4] += sum(maps[x + d2 + d][y + d2 - d + 1:])
    for i in range(x + d1 + d2 + 1, n1):
        cnt_list[4] += sum(maps[i][y - d1 + d2:])
    
    cnt_list[0] = total_sum - sum(cnt_list[1:])
    return max(cnt_list) - min(cnt_list)

min_val = 1e20
for x in range(1, n1):
    for y in range(1, n1):
        for d1 in range(1, n1):
            for d2 in range(1, n1):
                if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                    min_val = min(min_val, solution(x, y, d1, d2))
print(min_val)