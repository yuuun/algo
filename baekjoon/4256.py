t = int(input())

def get_postorder(preorder, inorder):
    if len(preorder) == 0:
        return
    if len(preorder) == 1:
        print(preorder[0], end=' ')
        return
    if len(preorder) == 2:
        print(preorder[1], preorder[0], end=' ')
        return 

    idx = inorder.index(preorder[0])
    left_in = inorder[0: idx]
    left_pre = preorder[1: 1 + len(left_in)]
    get_postorder(left_pre, left_in)
    
    right_in = inorder[idx + 1:]
    right_pre = preorder[len(left_in) + 1:]
    get_postorder(right_pre, right_in)
    print(preorder[0], end=' ')

for _ in range(t):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    get_postorder(preorder, inorder)
    print()
