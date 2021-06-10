n_room = int(input())
rooms = [1 for i in range(n_room)]

m = int(input())
if m == 0:
    print(n_room)

else:
    for _ in range(m):
        x, y = map(int, input().split())
        for i in range(x, y):
            rooms[i] = 0
    print(rooms[1:].count(1) + 1)