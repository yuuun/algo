## backtracking
## https://www.acmicpc.net/problem/15663
## TBD
'''
n, m = map(int, input().split())
com = sorted(list(map(int, input().split())))
tmp = []
ans = set()

def sol(depth, idx):
    global tmp
    if depth == m:
        ans.add(tmp)
        tmp = []
        return
    for i in range(idx, n):
        tmp.append(com[i])
        sol(depth + 1, i + 1)
        tmp.pop()
sol(0, 0)
print(ans)

'''
from itertools import combinations, permutations, product 
n, m = map(int, input().split()) 
a = list(map(int, input().split())) 

a.sort() 
cmb = list(permutations(a, m)) 
ans = [] 

for c in cmb: 
    ans.append(c)
ans = sorted(list(set(ans)))
     
for c in ans: 
    for i in c: 
        print(i, end=' ') 
    print()
