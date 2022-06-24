from collections import defaultdict

def find_parent(x):
    if x == parent[x]:
        return x
    else:
        root_x = find_parent(parent[x])
        parent[x] = root_x
        return parent[x]

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x != y:
        parent[y] = x
        number[x] += number[y]

for _ in range(int(input())):
    parent = defaultdict(int)
    number = defaultdict(int)
    for _ in range(int(input())):
        x, y = input().split()
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        union_parent(x, y)
        print(number[find_parent(x)])