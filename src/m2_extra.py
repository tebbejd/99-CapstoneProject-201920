"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Brandon Wohlfarth.
  Winter term, 2018-2019.
"""


def pickup_object_tone(frequency, speed, rate, robot):
    robot.go(speed, speed)
    initial = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    while True:
        dis = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if dis < initial:
            frequency = frequency * rate
            initial = dis
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 2:
            break
        robot.sound_system.tone_maker.play_tone(frequency, 1)
    robot.stop()
    robot.arm_and_claw.raise_arm()