n = int(input())
students = list(map(int, input().split()))

dp = [0] * n
for i in range(1, n):
    for k in range(1, i + 2):
        tmp = students[i - k + 1: i + 1]
        if k == i + 1: 
            k = i
        dp[i] = max(dp[i], dp[i - k] + abs(max(tmp) - min(tmp)))
print(dp[-1])

'''
시간초과!
memory = dict()
real_max = 0
for case in range(pow(2, len(students) - 1)):
    wall = [0 for _ in students[:-1]]
    t_case = case
    for i in range(len(wall)):
        wall[i] = t_case & 1
        t_case = t_case >> 1
    _sum = 0
    start = 0
    for i in range(len(students)):
        if i == len(students) - 1 or wall[i] == 1:
            end = i
            if '{}_{}'.format(start, end) in memory:
                _dif = memory['{}_{}'.format(start, end)]
            else:
                _max = students[start]
                _min = students[start]
                for j in range(start + 1, end + 1):
                    if students[j] > _max:
                        _max = students[j]
                    if students[j] < _min:
                        _min = students[j]
                _dif = _max - _min
                memory['{}_{}'.format(start, end)] = _dif
            _sum += _dif
            start = i + 1
    if _sum > real_max:
        real_max = _sum
print(real_max)
'''