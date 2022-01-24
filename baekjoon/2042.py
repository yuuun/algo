n, m, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
tree = [0] * (4 * n)
def init_seg(start, end, node):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    else:
        tree[node] = init_seg(start, (start + end) // 2, node * 2) + init_seg((start + end) // 2 + 1, end, node * 2 + 1)
        return tree[node]

def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    tree[node] += diff
    if start != end:
        update(node * 2, start, (start + end) // 2, idx, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, idx, diff)

def sumup(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]

    return sumup(node * 2, start, (start + end) // 2, left, right) + sumup(node * 2 + 1, (start + end) // 2 + 1, end, left, right)
init_seg(0, n - 1, 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        b -= 1
        diff = c - nums[b]
        nums[b] = c
        update(1, 0, n - 1, b, diff)
    if a == 2:
        print(sumup(1, 0, n - 1, b - 1, c - 1))