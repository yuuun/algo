n, ep, wp, np, sp = map(int, input().split())

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

prob = [0.01 * ep, 0.01 * wp, 0.01 * np, 0.01 * sp]
ans = 0


def dfs(x, y, visited, total):
    global ans
    if len(visited) == n + 1:
        ans += total
        return
    for idx, dd in enumerate(d):
        dx, dy = dd[0], dd[1]
        tx = x + dx
        ty = y + dy
        if (tx, ty) not in visited:
            visited.append((tx, ty))
            dfs(tx, ty, visited, total * prob[idx])
            visited.pop()

dfs(0, 0, [(0, 0)], 1)
print(ans)