alphabet = input()
ans = ""
for alpha in alphabet:
    val = ord(alpha) - ord("A") + 1
    ans += str(val) + " "
print(ans[:-1])