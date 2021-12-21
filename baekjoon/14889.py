# 시간 초과
n = int(input())
scores = [list(map(int, input().split())) for _ in range(n)]

all_sum = 0
for sc in scores:
    all_sum += sum(sc)
min_val = all_sum

visited = [0] * n
def cand(idx, cnt):
    global min_val
    if cnt == n / 2:
        s, l = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    s += scores[i][j]
                elif not visited[i] and not visited[j]:
                    l += scores[i][j]
        min_val = min(min_val, abs(s - l))
        return
    for i in range(idx, n):
        if visited[i]:
            continue
        visited[i] = 1
        cand(i + 1, cnt + 1)
        visited[i] = 0

cand(0, 0)
print(min_val)