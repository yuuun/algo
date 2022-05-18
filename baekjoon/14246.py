n = int(input())
arr = list(map(int, input().split()))
k = int(input())

cnt = 0
right = 0
sums = 0
for left in range(n):
    while sums <= k and right < n:
        sums += arr[right]
        right += 1
    if sums > k:
        cnt += n - right + 1
    sums -= arr[left]
print(cnt)