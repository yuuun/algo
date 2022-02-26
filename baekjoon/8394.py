# DP 연습  #마지막 자리만 본다
n = int(input())
a, b = 1, 0
for i in range(n):
    a, b = (a + b) % 10, a % 10
print(a)