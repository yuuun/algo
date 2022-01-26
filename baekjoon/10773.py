k = int(input())
fig = []
for _ in range(k):
    t = int(input())
    if t == 0:
        fig = fig[:-1]
    else:
        fig.append(t)
print(sum(fig))