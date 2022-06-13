def combination(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for j in combination(arr[i+1:], r - 1):
                yield [arr[i]] + j

def solution(line):
    answer = []
    arrs = []
    for n1, n2 in combination(line, 2):
        a, b, e = n1
        c, d, f = n2
        if a * d - b * c == 0:
            continue
        x = (b * f - e * d) / (a * d - b * c)
        if int(x) == x:
            y = (e * c - a * f) / (a * d - b * c)
            if int(y) == y:
                arrs.append([int(x), int(y)])
    rows = []
    cols = []
    for x, y in arrs:
        rows.append(x)
        cols.append(y)
    rows.sort()
    minR, maxR = rows[0], rows[-1]
    cols.sort()
    minC, maxC = cols[0], cols[-1]
    n, m = maxR - minR + 1, maxC - minC + 1
    
    for i in range(len(arrs)):
        arrs[i][0] = arrs[i][0] - minR
        arrs[i][1] = -arrs[i][1] + maxC
    
    answer = [['.'] * n for _ in range(m)]
    for y, x in arrs:
        answer[x][y] = '*'
    
    return [''.join(ans) for ans in answer]

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]), ["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"])
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))