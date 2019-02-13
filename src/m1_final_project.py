"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Jacob Tebbe.
  Winter term, 2018-2019.
"""


import time




def pickup_object(initial_beeping, increasing_beeping,robot):
    initial_beeping = initial_beeping.get()
    increasing_beeping = increasing_beeping.get()
    print(initial_beeping, increasing_beeping)
    robot.go(50, 50)
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() > 7:
            if time.time() % initial_beeping == 0:
                robot.sound_system.beeper.beep().wait()
        elif robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() >= 3:
            if time.time() % initial_beeping == 0:
                robot.sound_system.beeper.beep().wait()
        elif robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 3:
            robot.stop()
            robot.arm_and_claw.raise_arm()
            break


