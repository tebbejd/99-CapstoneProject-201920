"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Jacob Tebbe.
  Winter term, 2018-2019.
"""
import rosebot
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


