# https://kspsd.tistory.com/4
from collections import defaultdict
n, m = map(int, input().split())
folder = defaultdict(list)

for _ in range(n + m):
    a, b, c = input().split()
    folder[a].append((b, int(c)))

def find(target):
    global n_file, folder_set
    if target not in folder:
        return
    
    for info, c in folder[target]:
        if c == 0:
            folder_set.add(info)
            n_file += 1
        else:
            find(info)
    return

for _ in range(int(input())):
    loc = input().split('/')
    folder_set = set()
    n_file = 0
    find(loc[-1])

    print(len(folder_set), n_file)