n = int(input())
arr = list(map(int, input().split()))
m = int(input())
maps = sorted([(v, i) for i, v in enumerate(arr)], key=lambda x: (-x[0], -x[1]))
ans = ''
