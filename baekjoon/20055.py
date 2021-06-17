#deque: FIFO - 양방향 큐
from collections import deque
n, k = map(int, input().split())
belt = deque(list(map(int, input().split())))

ans = 1

robot = deque(list([0] * n))

while True:
    #하나씩 이동하기, robot이 마지막에 있을 경우에는 내리기 때문에 0으로 세팅
    belt.rotate(1)
    robot.rotate(1)
    robot[-1] = 0 

    #로봇 뒤에서부터 차례로 움직이는 내용 추가(robot위치 움직이고, belt의 수를 줄이기)
    for i in range(-2, -n-1, -1):
        if robot[i] == 1 and robot[i + 1] == 0 and belt[i + 1 - n] > 0:
            robot[i] = 0
            robot[i + 1] = 1
            belt[i + 1 - n] -= 1
    robot[-1] = 0

    #첫번째 위치에 로봇이 없을 경우 새로운 로봇을 올리기 
    if robot[0] == 0 and belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1
    
    if belt.count(0) >= k:
        break

    ans += 1
print(ans)