"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Brandon Wohlfarth.
  Winter term, 2018-2019.
"""


def pickup_object_tone(frequency, speed, rate, robot):
    robot.drive_system.go(speed, speed)
    initial = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    while True:
        dis = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if dis < initial:
            frequency = frequency * rate
            initial = dis
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 1:
            break
        robot.sound_system.tone_maker.play_tone(frequency, 1000)

        print(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()

def spin_pickup_clockwise(frequency, speed, rate, robot):
    robot.drive_system.spin_clockwise_until_sees_object(int(speed), 500)
    print("spin")
    robot.drive_system.go(speed, 0-speed)
    while True:
        b = robot.sensor_system.camera.get_biggest_blob()
        print(b.center.x)
        if b.center.x < 165 and b.center.x > 155:
            break
    robot.drive_system.stop()
    print("move with tone")
    pickup_object_tone(frequency, speed, rate, robot)

def spin_pickup_counterclockwise(frequency, speed, rate, robot):
    robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), 500)
    print("spin")
    robot.drive_system.go(0-speed, speed)
    while True:
        b = robot.sensor_system.camera.get_biggest_blob()
        print(b.center.x)
        if b.center.x < 165 and b.center.x > 155:
            break
    robot.drive_system.stop()
    print("move with tone")
    pickup_object_tone(frequency, speed, rate, robot)