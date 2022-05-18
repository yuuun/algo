n, k, b = map(int, input().split())
stick = [0] * n
for i in range(b):
    stick[int(input()) - 1] = 1

sums = sum(stick[:k])
min_val = sums 
for left, right in zip(range(0, n), range(k, n)):
    sums -= stick[left]
    sums += stick[right]
    if sums < min_val:
        min_val = sums
print(min_val)