def solution(numbers, hand):
    answer = ''
    maps = {0: [3, 1], 1: [0, 0], 2: [0, 1], 3:[0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2],
            7: [2, 0], 8: [2, 1], 9: [2, 2]}
    def get_dis(x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])
    lx, ly = 3, 0
    rx, ry = 3, 2
    for num in numbers:
        tx, ty = maps[num]
        if ty == 0: # 왼 손
            answer += 'L'
            lx, ly = tx, ty
        elif ty == 2: # 오른 손
            answer += 'R'
            rx, ry = tx, ty
        else:
            d1, d2 = get_dis([lx, ly], [tx, ty]), get_dis([rx, ry], [tx, ty])
            if d1 > d2:
                answer += 'R'
                rx, ry = tx, ty
            elif d1 < d2:
                answer += 'L'
                lx, ly = tx, ty
            else:
                if hand == 'left':
                    answer += 'L'
                    lx, ly = tx, ty
                else:
                    answer += 'R'
                    rx, ry = tx, ty
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],	"right"),	"LRLLLRLLRRL")
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],	"left"),	"LRLLRRLLLRR")
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],	"right"),	"LLRLLRLLRL")