#greedy
n, l = map(int, input().split())

water_list = []
for _ in range(n):
    water_list.append(list(map(int, input().split())))

water_list = sorted(water_list)

start = 0
res = 0
for water_s, water_e in water_list:
    start = max(water_s, start)
    rest = water_e - start
    tmp = (rest + l - 1) // l
    res += tmp
    start += tmp * l

print(res)