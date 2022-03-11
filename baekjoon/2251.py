from collections import deque


def pour(x, y):
    if not visited[x][y]:
        visited[x][y] = 1
        q.append((x, y))


def bfs():
    q.append((0,0))  # 처음 물통 a,b는 0,0
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        z = c - x - y  # z는 a와b에 의해 결정된다.
        if x == 0:  # 조건에서 a물통이 0일때 이므로
            answer.append(z)

        # a에서 b 물을 옮기는 경우
        if x > 0 and y < b:  # a에 물이 있고 b에 물이 가득차있지 않을 때
            w = min(x, b - y)
            pour(x - w, y + w)
        # a에서 c
        if x > 0 and z < c:
            w = min(x, c - z)
            pour(x - w, y)

        # b에서 a
        if y > 0 and x < a:
            w = min(y, a - x)
            pour(x + w, y - w)
        # b에서 c
        if y > 0 and z < c:
            w = min(y, c - z)
            pour(x, y - w)

        # c에서 a
        if z > 0 and x < a:
            w = min(z, a - x)
            pour(x + w, y)
        # c에서 b
        if z > 0 and y < b:
            w = min(z, b - y)
            pour(x, y + w)


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    # visited: a 물통과 b 물통의 양에 따라 c 물통의 양이 정해지기 때문에
    # a,b 두 통을 실행한 적이 있는지 확인하는 2중리스트
    visited = [[0] * (b + 1) for _ in range(a + 1)]
    # 답을 넣을 배열
    answer = []
    # BFS
    q = deque()
    bfs()
    # 답 출력
    answer.sort()
    print(' '.join(list(map(str, answer))))