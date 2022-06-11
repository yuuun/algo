def solution(sizes):
    width = []
    height = []
    for w, h in sizes:
        if w >= h:
            width.append(w)
            height.append(h)
        else:
            width.append(h)
            height.append(w)
    return max(width) * max(height)
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))