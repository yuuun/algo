#구현
loc = int(input()) - 1 # 0이나올 것을 대비해야됨!!
n = int(input())

cur_time = 0
li = []
for _ in range(n):
    li.append(list(map(str, input().split())))

for t, ans in li:
    cur_time += int(t)
    if 210 <= cur_time:
        break
    if ans == 'T':
        loc = (loc + 1) % 8

print(loc + 1)