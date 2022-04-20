r, c, k = map(int, input().split())
r, c = r - 1, c - 1
maps = [list(map(int, input().split())) for _ in range(3)]

def check_loc():
    if not (0 <= r < len(maps) and 0 <= c < len(maps[0])):
        return False
    if maps[r][c] == k:
        return True
    return False

from collections import Counter
def apply_R(x):
    global maps
    new = [[] for _ in range(x)]
    max_length = 0
    for i in range(x):
        tmp = Counter(maps[i])
        del tmp[0]
        tmp = sorted(tmp.items(), key=lambda x: (x[1], x[0]))
        tmp = tmp[:50]
        max_length = max(max_length, len(tmp))
        for t, v in tmp:
            new[i].extend([t, v])
    max_length *= 2
    for i in range(x):
        if max_length != len(new[i]):
            new[i] += [0] * (max_length - len(new[i]))
    return new

def transpose(arr):
    return [list(elem) for elem in zip(*arr)]

def apply_C():
    global maps
    maps = transpose(maps)
    maps = transpose(apply_R(len(maps)))
    return maps

cnt = 0
while cnt <= 100:
    if check_loc():
        break

    if len(maps) >= len(maps[0]):
        maps = apply_R(len(maps))
    else:
        maps = apply_C()
    cnt += 1

print(cnt if cnt != 101 else -1)