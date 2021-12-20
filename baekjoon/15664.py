n, m = map(int, input().split())
lis = sorted(list(map(int, input().split())))
tmp = []

def dfs(depth, idx):
    if m == depth:
        print(' '.join(map(str, tmp)))
        return
    prev = 0
    for i in range(idx, n):
        if prev == lis[i]:
            continue
        tmp.append(lis[i])
        dfs(depth + 1, i + 1)
        tmp.pop()
        prev = lis[i]

dfs(0, 0)