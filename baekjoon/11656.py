string = input()
lis = [string]
for i in range(1, len(string)):
    lis.append(string[i:])

for li in sorted(lis):
    print(li)