#TBD
t = int(input())
for _ in range(t):
    n = int(input())
    
    inp = [list(map(int, input().split())) for i in range(n + 2)]
    adj = [[0] * (n + 2) for i in range(n + 2)]
    print(inp)
    print(adj)