n, t, p = map(int, input().split())
p -= 1

total_time = set([])
reservation = [list(map(int, input().split())) for _ in range(t)]
reservation = sorted(reservation, key=lambda x: (x[0], x[1]))

for s, e in reservation:
    total_time.add(s)
    total_time.add(e)
total_time.add(900)
total_time = sorted(total_time)

seated = [[False] * n for _ in range(len(total_time))]

