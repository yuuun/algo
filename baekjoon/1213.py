names = input()
cnt_name = [0] * 26
for name in names:
    cnt_name[ord(name) - 65] += 1

odd = 0
odd_alpha = ''
alpha = ''

for i in range(26):
    if cnt_name[i] % 2 == 1:
        odd += 1
        odd_alpha += chr(i + 65)
    alpha += chr(i + 65) * (cnt_name[i] // 2)

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(alpha + odd_alpha + alpha[::-1])