n, m = map(int, input().split()) # n: 문자열 개수, m: 문자열 길이
arr = [''] * m

for _ in range(n):
    a = input()
    for i in range(m):
        arr[i] += a[i]

def check(k):
    tmp = set()
    for a in arr:
        string = a[k:]
        if string in tmp:
            return False
        else:
            tmp.add(string)
    return True

cnt = 0
top, bottom = 0, n - 1
while top <= bottom:
    mid = (top + bottom) // 2
    if check(mid):
        cnt = mid
        top = mid + 1
    else:
        bottom = mid - 1
print(cnt)
