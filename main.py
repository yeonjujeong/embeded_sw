#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor)
from pybricks.parameters import Port, Direction, Color
from pybricks.tools import wait
from pybricks.robotics import DriveBase

CONST_MOVE_AMOUNT = 18
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
    for i in range(10):
        # move belt
        sensor_motor.run_target(300,54*i,wait=True)
        # scan color
        check = sensor.color()
        show_screen(str(i*10)+"% / 100\n")
        ev3.screen.draw_text(40,100, str(check))
        result.append(convert_color(check, row, i))
        wait(500)
    # scan last color
    check = sensor.color()
    result.append(convert_color(check, row, i))

    return result
        


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

# Write your program here.
# ev3.speaker.beep()
ev3.screen.clear()
cur_row = 0
for row in range(10):
    cur_row = row
    arr.append(scan_map(row))
    if row < 9:
        # move to next row
        show_screen("Initializing...")
        sensor_motor.run_target(400, 0, wait=True)
        robot.straight(CONST_MOVE_AMOUNT)
    else:
        # move to start point at final
        print(start,"start")
        print(end,"end")
        move_col(start[1])
        cur_row = move_row(cur_row, start[0])
        wait(2000)
        move_col(end[1])
        cur_row = move_row(cur_row, end[0])

# reset to restart
move_col(0)
move_row(cur_row, 0)