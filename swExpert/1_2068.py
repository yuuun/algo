T = int(input())
for test_case in range(1, T + 1):
    inp = list(map(int, input().split()))
    ans = str(max(inp))
    print( "#" + str(test_case) + " " + ans)