#https://hillier.tistory.com/76
n = int(input())
n_student = n * n

order_dict = {}

for _ in range(n_student):
    pre = list(map(int, input().split()))
    order_dict[pre[0]] = pre[1:]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

arr = [[0] * n for _ in range(n)]
for key, values in order_dict.items():
    max_x = 0
    max_y = 0
    max_like = -1
    max_empty = -1

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                likecnt = 0
                emptycnt = 0
                for x, y in zip(dx, dy):
                    nx = i + x
                    ny = j + y
                    if 0 <= nx < n and 0 <= ny < n:
                        if arr[nx][ny] in values:
                            likecnt += 1
                        if arr[nx][ny] == 0:
                            emptycnt += 1
                if max_like < likecnt or (max_like == likecnt and max_empty < emptycnt):
                    max_x, max_y = i, j
                    max_like = likecnt
                    max_empty = emptycnt
    arr[max_x][max_y] = key

result = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        li = order_dict[arr[i][j]]
        for x, y in zip(dx, dy):
            nx = i + x
            ny = j + y
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] in li:
                    cnt += 1
        if cnt != 0:
            result += 10 ** (cnt - 1)
print(result)


#https://hbj0209.tistory.com/84
'''
from collections import defaultdict
import sys
input = sys.stdin.readline
N = int(input())
m = [[0] * N**2 for _ in range(N**2)]
student_list = defaultdict(list)
for _ in range(N**2):
	student, *s = map(int,input().split())
	student_list[student] = s
dx, dy = [0,0,-1,1], [-1,1,0,0]
 
# 1번조건 check
def first_check(i, j, st):
	cnt = 0
	for x in range(4):
		nx, ny = i + dx[x], j + dy[x]
		if 0 <= nx < N and 0 <= ny < N and m[nx][ny] in student_list[st]:
			cnt += 1
	return cnt
 
# 2번조건 check
def second_check(i, j):
	cnt = 0
	for x in range(4):
		nx, ny = i + dx[x], j + dy[x]
		if 0 <= nx < N and 0 <= ny < N and m[nx][ny] == 0:
			cnt += 1
	return cnt
 
# 만족도 구하는 함수
def happy(i, j):
	cnt = 0
	happy_cnt = [0,1,10,100,1000]
	for x in range(4):
		nx, ny = i + dx[x], j + dy[x]
		if 0 <= nx < N and 0 <= ny < N and m[nx][ny] in student_list[m[i][j]]:
			cnt += 1
	return happy_cnt[cnt]
 
for st in student_list:
	dic = defaultdict(list)
	for i in range(N):
		for j in range(N):
			if m[i][j] == 0:
				dic[first_check(i, j, st)].append((i, j))
    	# dic의 key순으로 내림차순 정렬 -> 좋아하는 학생이 많은 칸 순서대로 정렬됨
	s = sorted(dic.items(), key = lambda x: -x[0])
    	# 1번 조건만족하는 칸이 여러개이면 2번조건으로 넘어감
	if len(dic[s[0][0]]) > 1:
		dic2 = defaultdict(list)
		for i,j in dic[s[0][0]]:
			dic2[second_check(i, j)].append((i, j))
        	# dic2의 key순으로 내림차순 정렬 -> 비어있는 칸이 많은 순서대로 정렬됨
		s = sorted(dic2.items(), key = lambda x: -x[0])
        	# 2번 조건 만족하든 안하든 좌표가 (0, 0) 부터 정렬되어있으므로 첫번째 좌표에 st넣어줌
		m[dic2[s[0][0]][0][0]][dic2[s[0][0]][0][1]] = st
	else:
		m[dic[s[0][0]][0][0]][dic[s[0][0]][0][1]] = st
 
dab = 0
for i in range(N):
	for j in range(N):
		dab += happy(i, j)
print(dab)

'''