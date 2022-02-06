import sys
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    closest = sys.maxsize
    for i in range(n):
        s, e = i + 1, n - 1
        while s <= e:
            m = (s + e) // 2
            t = nums[i] + nums[m]

            if t > k:
                e = m - 1
            else:
                s = m + 1
            
            if abs(k - t) < closest:
                cnt = 1
                closest = abs(k - t)
            elif abs(k - t) == closest:
                cnt += 1
    print(cnt)