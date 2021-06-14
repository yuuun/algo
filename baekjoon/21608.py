n = int(input())
n_student = n * n

#fail
order_dict = {}

for _ in range(n_student):
    pre = list(map(int, input().split()))
    order_dict[pre[0]] = pre[1:]

arr = [[0] * n for _ in range(n)]
for _ in range(n_student):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                lc = 0


def isadj(li1, li2):
    dist = 0
    for l1, l2 in zip(li1, li2):
        dist += abs(l1 - l2)
    
    if dist == 1:
        return True
    else:
        return False