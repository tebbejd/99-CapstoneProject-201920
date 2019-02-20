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
    print("Quiet Hours stop")
def rounds(robot, speed):
    print('Begin Rounds')
    if speed <= 10:
        return None
    for j in range(4):
        print(j)
        robot.drive_system.go_straight_for_inches_using_encoder(36, speed)
        robot.drive_system.go(speed, 0 - speed)
        start = time.time()
        while True:
            print(robot.sensor_system.camera.get_biggest_blob().get_area())
            if robot.sensor_system.camera.get_biggest_blob().get_area() >= 200:
                robot.drive_system.stop()
                time_tot = time.time()-start
                robot.sound_system.speech_maker.speak("Hello, how are you?")
                time.sleep(3)
                start = time.time()
                robot.drive_system.go(0-speed, speed)
                while True:
                    if time.time() - start >= time_tot:
                        robot.drive_system.stop()
                        break
                break
    robot.sound_system.speech_maker.speak("Time for bed")
    print("Rounds over")

def floor_dinner(robot, string):
    print("floor dinner start")
    robot.drive_system.go(30, 30)
    for k in range(3):
        print(k)
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 3:
            break
        robot.sound_system.speech_maker.speak(string)
        time.sleep(3)
    robot.drive_system.stop()
    print("floor dinner stop")

def inspect(robot):
    print('inspection start')
    robot.sound_system.speech_maker.speak("How is everyone tonight")
    robot.drive_system.go_straight_for_inches_using_encoder(36, 100)
    robot.drive_system.go(30, -30)
    time_int = time.time()
    print("spin")
    while True:
        b = robot.sensor_system.camera.get_biggest_blob()
        print(b.center.x)
        if b.center.x < 165 and b.center.x > 155:
            break
    time_tot = time.time() - time_int
    robot.drive_system.stop()
    robot.drive_system.go(50, 50)
    time2 = time.time()
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 1:
            break
        print(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
    robot.drive_system.stop()
    time_tot2 = time.time() - time2
    robot.arm_and_claw.raise_arm()
    robot.sound_system.speech_maker.speak("I have to dump this")
    robot.drive_system.go_straight_for_seconds(time_tot2, -50)
    start = time.time()
    robot.drive_system.go(-30, 30)
    while True:
        if time.time() - start >= time_tot:
            robot.drive_system.stop()
            break
    robot.drive_system.go_straight_for_inches_using_encoder(36, -100)
    robot.arm_and_claw.lower_arm()
    print('inspection complete')

def make_fun(robot, string):
    print('joke start')
    robot.sound_system.speech_maker.speak(string)
    print('joke done')