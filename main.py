#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor)
from pybricks.parameters import Port, Direction, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from collections import deque

CONST_MOVE_AMOUNT = 18.5
arr = []
global start, end

def show_screen(str):
    ev3.screen.clear()
    ev3.screen.draw_text(40, 50, str)
    
def move_col(target):
    sensor_motor.run_target(400, 54*target, wait=True)

def move_row(cur, target):
    robot.straight((target-cur)*CONST_MOVE_AMOUNT)
    return target
    
def convert_color(check, row, i):
    if check == Color.BLACK:
        return 1
    else:
        if check == Color.GREEN:
            print("find green at [", row, i,"]" )
            global start
            start = [row, i]
        elif check == Color.RED:
            print("find RED")
            global end
            end = [row, i]
        return 0

def scan_map(row):
    result = []
    sequence = []
    if row % 2 == 0: sequence = range(10)
    else: sequence = range(9, -1, -1)
    for i in sequence:
        # move belt
        sensor_motor.run_target(250,54*i,wait=True)
        wait(200)
        # scan color
        check = sensor.color()
        show_screen(str(i*10)+"% / 100\n")
        ev3.screen.draw_text(40,100, str(check))
        result.append(convert_color(check, row, i))
        wait(200)
    # # scan last color
    # check = sensor.color()
    # result.append(convert_color(check, row, i))
    if row % 2 == 0: return result
    else: 
        result.reverse()
        return result
        
def bfs(root):
    visited = [[0] * 10 for _ in range(10)]
    queue = deque([root])
    route_q = deque([[root]])
    
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    
    visited[root[0]][root[1]] = 1

    while queue:
        now = queue.popleft()
        route = route_q.popleft()
        global end
        if now[0] == end[0] and now[1] == end[1]: #end에 도착하면 끝내기
            return route
        for i in range(4):
            route_tmp = []
            for tmp in route:
                route_tmp.append(tmp)
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]
            if nx < 0 or nx >= 10 or ny < 0 or ny >= 10:
                continue
            if arr[nx][ny] == 1 or visited[nx][ny] == 1:
                continue
            route_tmp.append([nx, ny])
            route_q.append(route_tmp)
            queue.append([nx, ny])        
            visited[nx][ny] = 1 

# Create your objects here.
ev3 = EV3Brick()
ev3.screen.clear()
# test_motor = Motor(Port.B)
sensor_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE, gears=[10])
left_motor = Motor(Port.D)
right_motor = Motor(Port.A)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
robot.settings(straight_speed=40)
sensor = ColorSensor(Port.S2)

print(arr)
print("HEllo")

# Write your program here.
# ev3.speaker.beep()
ev3.screen.clear()
cur_row = 0
for row in range(10):
    cur_row = row
    arr.append(scan_map(row))
    if row < 9:
        # move to next row
        robot.straight(CONST_MOVE_AMOUNT)
    else:
        # move to start point at final
        global start
        global end
        print(start,"start")
        print(end,"end")
        move_col(start[1])
        cur_row = move_row(cur_row, start[0])
        wait(2000)
        move_col(end[1])
        cur_row = move_row(cur_row, end[0])
print(arr)
print("HEllo")
print(str(arr[0][0]) + " is 0, 0.")

# find path
path = bfs(start)
print(path)

# drive the path
# path = [[0, 1], [1, 1], [2, 1], [2, 2], [2, 3], [3, 3], [4, 3], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [6, 7], [7, 7], [7, 6], [7, 5], [8, 5], [9, 5]]
for now in path :
    move_col(now[1])
    cur_row = move_row(cur_row, now[0])
    print(now)
    print("is now")


