def solution(files):
    splited = []
    for file in files:
        idx = 0
        while idx < len(file) and not file[idx].isdigit():
            idx += 1
        idx_ = idx
        while idx_ < len(file) and file[idx_].isdigit():
            idx_ += 1
        splited.append([file[:idx].lower(), int(file[idx:idx_]), file[idx_:], file])
    splited = sorted(splited, key=lambda x:(x[0], x[1]))
    answer = [split[-1] for split in splited]
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]), ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"])