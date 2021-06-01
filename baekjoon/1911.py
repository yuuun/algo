n, l = map(int, input().split())

water_list = []
for _ in range(n):
    water_list.append(list(map(int, input().split())))

water_list = sorted(water_list)

pan_list = ['.' for i in range(water_list[-1][1])]

for pan in range(l):
    pan_list[pan] = 1
if water_list[0][0] < l:
    water_list[0][0] = 1

ant = 2
for fir, end in water_list:
    tmp = fir
    while pan_list[tmp] != '.' and tmp < end:
        tmp += 1
    
    while tmp < end:
        print(pan_list, tmp, end)
        for le in range(l):
            if tmp == water_list[-1][1]:
                break
            pan_list[tmp] = ant
            tmp += 1
        ant += 1

print(ant - 1)