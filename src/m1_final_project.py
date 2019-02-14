"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Jacob Tebbe.
  Winter term, 2018-2019.
"""
import rosebot
import time
def pickup_object_beep(initial_beeping, increasing_beeping,robot):

    print(initial_beeping, increasing_beeping)
    robot.drive_system.go(35, 35)
    count = 0
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() > 15:
            if count % float(initial_beeping) == 0:
                robot.sound_system.beeper.beep().wait()
                count = 0
        elif robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() >= .7:
            if count % float(increasing_beeping) == 0:
                robot.sound_system.beeper.beep().wait()
                count =0
            count += .5
        elif robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < .6:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break
        count += .5


def pickup_object_leds(initial_cycle, increasing_cycle,robot):

    print(initial_cycle, increasing_cycle)
    robot.drive_system.go(35, 35)
    count = 0
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() > 15:
            if count % float(initial_cycle) == 0:
                led_cycle()
                count = 0
        elif robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() >= .7:
            if count % float(increasing_cycle) == 0:
                led_cycle()
                count =0
            count += .5
        elif robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < .6:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break
        count += .5

def led_cycle():
    left_led = rosebot.LED('left')
    right_led = rosebot.LED('right')
    left_led.turn_on().wait()
    left_led.turn_off().wait()
    right_led.turn_on().wait()
    right_led.turn_off().wait()
    left_led.turn_on().wait()
    right_led.turn_on().wait()
    left_led.turn_off().wait()
    right_led.turn_off().wait()

def spin_then_pickup(direction,speed,robot):
    print('hewwo')
    if direction is 'CW':
        print('spinng clockwise at speed',speed)
        robot.drive_system.spin_clockwise_until_sees_object(int(speed), 500)
        robot.drive_system.go(100, -100)
        time.sleep(.1)
    else:
        print('spinning counterclockwise at speed',speed)
        robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), 500)
        robot.drive_system.go(-100, 100)
        time.sleep(.1)
    pickup_object_beep(5,1,robot)

def spin_then_pickup_leds(direction,speed,robot):
    if direction is 'CW':
        print('spinng clockwise at speed',speed)
        robot.drive_system.spin_clockwise_until_sees_object(int(speed), 500)
        robot.drive_system.go(100,-100)
        time.sleep(.1)
    else:
        print('spinning counterclockwise at speed',speed)
        robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), 500)
        robot.drive_system.go(-100,100)
        time.sleep(.1)
    pickup_object_leds(5,1,robot)