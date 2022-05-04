def is_place(x, y):
    if 0 <= x < 5 and 0 <= y < 5:
        return True
    return False
def replace_place(place):
    for x in range(5):
        for y in range(5):
            if place[x][y] == 'P':
                # 1
                nx, ny = x + 1, y
                if is_place(nx, ny) and place[nx][ny] == 'P':
                    return False
                nx, ny = x, y + 1
                if is_place(nx, ny) and place[nx][ny] == 'P':
                    return False

                # 2
                nx, ny = x + 1, y + 1
                if is_place(nx, ny):
                    if place[nx][ny] == 'P':
                        if place[x + 1][y] == 'O' or place[x][y + 1] == 'O':
                            return False
                nx, ny = x - 1, y + 1
                if is_place(nx, ny):
                    if place[nx][ny] == 'P':
                        if place[x - 1][y] == 'O' or place[x][y + 1] == 'O':
                            return False
                nx, ny = x + 1, y - 1
                if is_place(nx, ny):
                    if place[nx][ny] == 'P':
                        if place[x + 1][y] == 'O' or place[x][y - 1] == 'O':
                            return False
                
                nx, ny = x + 2, y
                if is_place(nx, ny):
                    if place[nx][ny] == 'P':
                        if place[x + 1][y] == 'O':
                            return False
                nx, ny = x, y + 2
                if is_place(nx, ny):
                    if place[nx][ny] == 'P':
                        if place[x][y + 1] == 'O':
                            return False
    return True
def solution(places):
    answer = []
    for place in places:
        if replace_place(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]), [1, 0, 1, 1, 1])