n = int(input())
str2 = '@' * n
str1 = (str2 * 5 + '\n') * n
print(str1, end='')
for _ in range(4 * n):
    print(str2)
