T = int(input())

for test_case in range(1, T + 1):
    inp = map(int, input().split())
    su = 0
    for i in inp:
        if i % 2 == 1:
            su += i
    print("#" + test_case + " " +su)