from collections import defaultdict
n, m = map(int, input().split())

bridge = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    bridge[a].append([b, c])
    bridge[b].append([a, c])

print(bridge)
s, e = map(int, input().split())
def get_bridge():
    for a, b in bridge[s]:
        if a == e:
            print(e)
    return