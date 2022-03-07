# 3:38 - 3:58
'''
n = int(input())
a = list(map(int, input().split()))
operator = list(map(int, input().split()))  
comb_op = []    #덧셈, 뺄셈, 곱셈, 나눗셈
for i, op in enumerate(operator):
    comb_op += [i] * op

def permutation(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for j in permutation(arr[:i] + arr[i + 1:], r - 1):
                yield [arr[i]] + j


cand = []
cnt = 0
for ops in permutation(comb_op, n - 1):
    ans = a[0]
    for num, op in zip(a[1:], ops):
        if op == 0:
            ans += num
        elif op == 1:
            ans -= num
        elif op == 2:
            ans *= num
        else:
            ans = int(ans / num)
    cand.append(ans)

print(max(cand))
print(min(cand))
'''

# 4:02 - 4:13
n = int(input())
a = list(map(int, input().split()))
operator = list(map(int, input().split()))

ans = []
def dfs(cur_num, idx):
    if idx == n:
        ans.append(cur_num)
        return
    for j in range(len(operator)):
        cur = cur_num
        if operator[j] != 0:
            if j == 0:
                cur += a[idx]
            elif j == 1:
                cur -= a[idx]
            elif j == 2:
                cur *= a[idx]
            else:
                cur = int(cur / a[idx])
            
            operator[j] -= 1
            dfs(cur, idx + 1)
            operator[j] += 1
    

dfs(a[0], 1)
print(max(ans))
print(min(ans))