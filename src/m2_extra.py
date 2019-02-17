"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Brandon Wohlfarth.
  Winter term, 2018-2019.
"""
import time

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

def quiet_hours(robot, n):
    print('Execute Quiet Hours Command')
    robot.sound_system.speech_maker.speak(n)

def rounds(robot, speed):
    print('Begin Rounds')
    for j in range(4):
        robot.drive_system.go_straight_for_inches_using_encoder(84, speed)
        robot.drive_system.go(speed, 0 - speed)
        start = time.time()
        while True:
            print(robot.sensor_system.camera.get_biggest_blob().get_area())
            if robot.sensor_system.camera.get_biggest_blob().get_area() >= 200:
                robot.stop()
                robot.sound_system.speech_maker.speak("Hello, how are you?")
                robot.drive_system.go(speed, 0 - speed)
            if time.time() - start >= 15:
                robot.drive_system.stop()
                break
    print('time for bed')

def floor_dinner(robot, string):
    robot.drive_system.go(100, 100)
    for k in range(10):
        robot.sound_system.speech_maker.speak(string)
        time.sleep(5)
    robot.drive_system.stop()

def inspect(robot):
    robot.sound_system.speech_maker.speak("Someone told me you have beer")
    robot.drive_system.go_straight_for_inches_using_encoder(84, 100)
    robot.drive_system.go(30, -30)
    print("spin")
    while True:
        b = robot.sensor_system.camera.get_biggest_blob()
        print(b.center.x)
        if b.center.x < 165 and b.center.x > 155:
            break
    robot.drive_system.stop()
    robot.drive_system.go(50, 50)
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 1:
            break
        print(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()
    robot.sound_system.speech_maker.speak("I have to dump this")

def make_fun(robot, string):
    robot.sound_system.speech_maker.speak(string)