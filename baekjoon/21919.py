n = int(input())
nums = set(map(int, input().split()))
ans = 1
for num in nums:
    isTrue = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            isTrue = False
            break
    if isTrue:
        ans *= num
print(ans if ans != 1 else -1)