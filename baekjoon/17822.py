from collections import deque
n, m, t = map(int, input().split())
circle = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    circle.append(deque(tmp))

def deepcopy(arr):
    new_arr = []
    for ar in arr:
        q = deque()
        for a in ar:
            q.append(a)
        new_arr.append(q)
    return new_arr

def remove_num():
    new_circle = deepcopy(circle)

    flag = True
    #같은 원판에 인접한 수 제거
    for j, cir in enumerate(circle):
        for i in range(-1, len(cir) - 1):
            if cir[i] == cir[i + 1] and cir[i] != 'x':
                new_circle[j][i] = 'x'
                new_circle[j][i + 1] = 'x'
                flag = False
    
    #원판 사이에 인접한 수 제거
    for j in range(m):
        for i in range(n - 1):
                if circle[i][j] == circle[i + 1][j] and circle[i][j] != 'x':
                    new_circle[i][j] = 'x'
                    new_circle[i + 1][j] = 'x'
                    flag = False
                
    # 변경한 것이 없다면, 
    if flag:
        sum_val, cnt = 0, 0
        for cir in new_circle:
            for c in cir:
                if c != 'x':
                    cnt += 1
                    sum_val += c
        if cnt != 0:
            avg = sum_val / cnt
            
            for i, cir in enumerate(new_circle):
                for j, c in enumerate(cir):
                    if c != 'x':
                        if c > avg:
                            new_circle[i][j] -= 1
                        elif c < avg:
                            new_circle[i][j] += 1
        
    return new_circle

def cnt_sum():
    ans = 0
    for cir in circle:
        for c in cir:
            if c != 'x':
                ans += c
    return ans

for _ in range(t):
    i, d, k = map(int, input().split())
    k = k if d == 0 else -k
    for t in range(i, n + 1, i):
        circle[t - 1].rotate(k)
    circle = remove_num()
    # print(circle)
print(cnt_sum())