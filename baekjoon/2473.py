#TBD
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
left, right = 0, n - 1
sums = arr[left] + arr[right]
