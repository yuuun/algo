#구현
n = int(input())
c = int(input())

p_list = list(map(int, input().split()))
li = []
cnt_list = []   #[추천 받은 수, 타이밍]

for t, k in enumerate(p_list):
    #이미 값이 있을 경우에는 update
    if k in li:
        ind = li.index(k)
        cnt_list[ind] = [cnt_list[ind][0] + 1, t]

    #액자에 아무도 안 들어갔을 경우
    elif len(li) < n:
        li.append(k)
        cnt_list.append([1, t])

    #나머지 경우에는 sorting한 다음에 가장 첫번째 있는 값으로 액자를 대체
    else:
        sorted_cnt = sorted(range(len(cnt_list)), key=lambda x: (cnt_list[x][0], cnt_list[x][1]))
        kk = sorted_cnt[0]
        li[kk] = k
        cnt_list[kk] = [1, t]

print(' '.join([str(e) for e in sorted(li)]))