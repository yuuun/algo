n = int(input())  # 도시의 개수
m = int(input())  # 버스의 개수

route = []
for _ in range(m):
    route.append(list(map(int, input().split())))

start, end = map(int, input().split())
