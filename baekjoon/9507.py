n = int(input())
inp = []
ans = [1, 1, 2, 4]

for _ in range(n):
    inp.append(int(input()))
max_val = max(inp)

for idx in range(4, max_val + 1):
    ans.append(ans[idx - 4] + ans[idx - 3] + ans[idx - 2] + ans[idx - 1])

for i in inp:
    print(ans[i])