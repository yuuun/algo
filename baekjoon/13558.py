# from collections import Counter
n = int(input())
nums = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # print(i, j, k)
            a, b, c = nums[i], nums[j], nums[k]
            if a + c == 2 * b:
                # print(a, b, c, i, i + j, i + j + j)
                ans += 1
print(ans)
# cnts = Counter(nums)

# figs = sorted([*cnts])
# ans = 0
# for idx, cnt in cnts.items():
#     if cnt == 3:
#         ans += 1
# print(figs)

# for i in range(len(figs) - 2):
#     for j in range(1, (len(figs) - i) // 2):
#         a, b, c = figs[i], figs[i + j], figs[i + 2 * j]
#         if a + c == 2 * b:
#             print(a, b, c, cnts[a], cnts[b], cnts[c])
#             ans +=  cnts[a] * cnts[b] * cnts[c]
# print(ans)
