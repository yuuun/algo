#sliding window - 두 arr를 합쳐주어야 함
from collections import defaultdict

n, d, k, c = map(int, input().split())
belt = [int(input()) for _  in range(n)]
belt += belt

left, right, cnt = 0, 0, 0
info = defaultdict(int)
info[c] += 1
for right in range(len(belt)):
    info[belt[right]] += 1
    if right >= k - 1:
        cnt = max(cnt, len(info))
        info[belt[left]] -= 1
        if info[belt[left]] == 0:
            del info[belt[left]]
        left += 1
print(cnt)