#greedy algorithm
expression = input()
exp_arr = expression.split('-')
ans = 0

for e in map(int, exp_arr[0].split('+')):
    ans += e

for exp in exp_arr[1:]:
    ex = exp.split('+')
    for e in ex:
        ans -= int(e)

print(ans)