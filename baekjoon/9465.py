#dp
t = int(input())
for _ in range(t):
    n = int(input())
    stick = []
    for _ in range(2):
        stick.append(list(map(int, input().split())))
    
    if n > 1:
        stick[0][1] += stick[1][0]
        stick[1][1] += stick[0][0]
        for j in range(2, n):
            stick[0][j] += max(stick[1][j-1], stick[1][j-2])
            stick[1][j] += max(stick[0][j-1], stick[0][j-2])
    print(max(stick[0][n - 1], stick[1][n - 1]))