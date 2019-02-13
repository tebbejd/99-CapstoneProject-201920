"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Jacob Tebbe.
  Winter term, 2018-2019.
"""


import time




def pickup_object(initial_beeping, increasing_beeping,robot):

    print(initial_beeping, increasing_beeping)
    robot.drive_system.go(35, 35)
    count = 0
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() > 10:
            if count % float(initial_beeping) == 0:
                robot.sound_system.beeper.beep().wait()
        elif robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() >= .7:
            if count % float(increasing_beeping) == 0:
                robot.sound_system.beeper.beep().wait()
        elif robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < .6:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break
        count += 1


