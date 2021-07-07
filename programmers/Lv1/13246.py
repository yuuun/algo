from collections import defaultdict
my_str = input().strip()
ans = defaultdict(int)
for my in my_str:
    ans[my] += 1
ans = {k: v for k, v in sorted(ans.items(), key=lambda item: item[1], reverse=True)}

max_val = 0
answer = []
for k, v in ans.items():
    if v >= max_val:
        max_val = v
        answer.append(k)
    else:
        break
print(''.join(map(str, sorted(answer))))
