n = int(input())
cnt = 0
for i in range(n):
    word = input()
    isGroup = True
    w1 = word[0]
    alpha_list = [w1]

    for w in word[1:]:
        if w == w1:
            continue
        elif w in alpha_list:
            isGroup = False
            break
        else:
            alpha_list.append(w)
            w1 = w
    if isGroup:
        cnt += 1
print(cnt)