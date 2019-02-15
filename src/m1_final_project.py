"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Jacob Tebbe.
  Winter term, 2018-2019.
"""
import rosebot
import time


def pickup_object_beep(initial_beeping, increasing_beeping, robot):
    print(initial_beeping, increasing_beeping)
    robot.drive_system.go(35, 35)
    count = 0
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() > 15:
            if count % float(initial_beeping) == 0:
                robot.sound_system.beeper.beep().wait()
                count = 0
        elif robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() >= 1.2:
            if count % float(increasing_beeping) == 0:
                robot.sound_system.beeper.beep().wait()
                count = 0
            count += .5
        elif robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 1.1:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break
        count += .5


def pickup_object_leds(initial_cycle, increasing_cycle, robot):
    print(initial_cycle, increasing_cycle)
    robot.drive_system.go(35, 35)
    count = 0
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() > 15:
            if count % float(initial_cycle) == 0:
                led_cycle()
                count = 0
        elif robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() >= 1.2:
            if count % float(increasing_cycle) == 0:
                led_cycle()
                count = 0
            count += .5
        elif robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 1.1:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break
        count += .5


def led_cycle():
    left_led = rosebot.LED('left')
    right_led = rosebot.LED('right')
    left_led.turn_on()
    left_led.turn_off()
    right_led.turn_on()
    right_led.turn_off()
    left_led.turn_on()
    right_led.turn_on()
    left_led.turn_off()
    right_led.turn_off()


def spin_then_pickup(direction, speed, robot):
    print('hewwo')
    if direction[1] == 'w':
        print('spinng clockwise at speed', speed)
        robot.drive_system.spin_clockwise_until_sees_object(int(speed), 500)
        spin_to_center(robot, direction)

    else:
        print('spinning counterclockwise at speed', speed)
        robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), 500)
        spin_to_center(robot, direction)
    pickup_object_beep(5, 1, robot)
    return


def spin_then_pickup_leds(direction, speed, robot):
    if direction[1] == 'w':
        print('spinnig clockwise at speed', speed)
        robot.drive_system.spin_clockwise_until_sees_object(int(speed), 500)
        spin_to_center(robot, direction)
    else:
        print('spinning counterclockwise at speed', speed)
        robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), 500)
        spin_to_center(robot, direction)
    pickup_object_leds(5, 1, robot)
    return


def spin_to_center(robot, direction):
    while True:
        if direction[1] == 'w':
            robot.drive_system.go(25, 0 - 25)
        else:
            robot.drive_system.go(0 - 25, 25)
        b = robot.sensor_system.camera.get_biggest_blob()
        print(b.center.x)
        if b.center.x <= 165 and b.center.x >= 155:
            robot.drive_system.stop()
            break

def start_destruction(answer,speed,robot):
    if answer == 'yes':
        print('My speed is set to', speed)
    else:
        print('I will wait until you are ready')
        return

def survey_site(robot):
    pass

def head_towards_site(robot):
    pass

def run_away(robot):
    pass