n, m, k = map(int, input().split())
power = list(map(int, input().split()))
parent = [i for i in range(n + 1)]
weight = []
for i in range(m):
    weight.append(list(map(int, input().split())))

weight = sorted(weight, key=lambda x: x[2])

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    x, y = find_parent(x), find_parent(y)
    if x != y:
        parent[y] = x

# 발전소를 하나의 집합으로 설정하기
for i in range(len(power) - 1):
    union_parent(power[i], power[i + 1])
# 결과: [0, 1, 1, 3, 4, 5, 6, 7, 8, 1]

res = 0
for a, b, c in weight:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        res += c

print(res)