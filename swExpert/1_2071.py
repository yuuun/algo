T = int(input())
for test_case in range(1, T + 1):
    inp = list(map(int, input().split()))
    su = 0
    for i in inp:
        su += i
    su = round(su / len(inp))
    print( "#" + str(test_case) + " " + str(su))