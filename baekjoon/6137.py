from collections import deque
n = int(input())
s = deque()
for _ in range(n):
    s.append(input())

t = ''
cnt = 0
start, end = 0, n - 1
while start <= end:
    if s[start] < s[end]:
        t += s[start]
        start += 1
    elif s[start] > s[end]:
        t += s[end]
        end -= 1
    else:
        st, se = start, end
        flag = False
        while st <= se:
            if s[st] < s[se]:
                t += s[start]
                start += 1
                flag = True
                break
            elif s[st] > s[se]:
                t += s[end]
                end -= 1
                flag = True
                break
            else:
                st += 1
                se -= 1
        if not flag:
            t += s[start]
            start += 1
    cnt += 1
    if cnt % 80 == 0:
        t += '\n'
print(t)