num = int(input())
numbers = list(map(int, input().split()))
cnt = 0
for nums in numbers:
    if nums == 1 or nums == 4:
        continue
    else:
        isPrime = True
        for n in range(2, int(nums/2)):
            if nums % n == 0:
                isPrime = False
                break
        if isPrime:
            cnt += 1

print(cnt)