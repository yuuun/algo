x, y, w, s = map(int, input().split())


if 2 * w > s:
    min_val = min(x, y)
    max_val = max(x, y)

    if w >= s:
        tmp = (x + y) % 2
        print((max_val - tmp) * s + tmp * w)
    else:
        print(min_val * s + (max_val - min_val) * w)
else:
    print((x + y) * w)