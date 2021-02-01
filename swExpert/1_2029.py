T = int(input())
for idx in range(1, T + 1):
    a, b = map(int, input().split())
    print("#" + str(idx) + " " + str(a // b), " " + str(a % b))