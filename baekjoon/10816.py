#a list에 대하여 각각이 몇개 있는지 저장하는 방식으로 dictionary를 정의해야 함.
n, a = int(input()), sorted(list(map(int, input().split())))
m, b = int(input()), list(map(int, input().split()))

def binary_search(bb, start, end):
    if start > end:
        return 0
    m = (start + end) // 2
    if bb == a[m]:
        return a[start: end + 1].count(bb)
    elif bb < a[m]:
        return binary_search(bb, start, m - 1)
    else:
        return binary_search(bb, m + 1, end)

n_dic = {}

for aa in a:
    if aa not in n_dic:
        n_dic[aa] = binary_search(aa, 0, n - 1)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in b))