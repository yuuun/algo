T = int(input())
for test_case in range(1, T + 1):
    inp = list(map(int, input().split()))
    ans = ""
    if inp[0] == inp[1]:
        ans = "="
    elif inp[0] > inp[1]:
        ans = ">"
    else:
        ans = "<"
    print( "#" + str(test_case) + " " + ans)