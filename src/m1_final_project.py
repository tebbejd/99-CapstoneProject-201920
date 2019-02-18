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
        b = robot.sensor_system.camera.get_biggest_blob().get_area()
        if b <= 60 and b >= 50:
            robot.drive_system.stop()
            break


def start_destruction(answer, speed, robot):
    if answer == 'yes':
        print('My speed is set to', speed)
        destroy(robot, speed)

    else:
        print('I will wait until you are ready')
        robot.sound_system.speech_maker.speak('I will wait until you are ready')


def survey_site(robot):
    robot.drive_system.go_straight_until_intensity_is_less_than(10, 50)
    robot.drive_system.go_straight_until_intensity_is_greater_than(60, 50)
    spin_to_center(robot, 'ccw')
    for k in range(3):
        robot.drive_system.go_straight_until_intensity_is_greater_than(60, 50)
        spin_to_center(robot, 'ccw')


def head_towards_site(robot):
    spin_to_center(robot, 'ccw')
    robot.drive_system.go_straight_for_inches_using_encoder(12, 50)


def go_on_break(robot):
    robot.sound_system.tone_maker.play_tone_sequence([
        (392, 350, 100), (392, 350, 100), (392, 350, 100), (311.1, 250, 100),
        (466.2, 25, 100), (392, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
        (392, 700, 100), (587.32, 350, 100), (587.32, 350, 100),
        (587.32, 350, 100), (622.26, 250, 100), (466.2, 25, 100),
        (369.99, 350, 100), (311.1, 250, 100), (466.2, 25, 100),
        (392, 700, 100),
        (784, 350, 100), (392, 250, 100), (392, 25, 100), (784, 350, 100),
        (739.98, 250, 100), (698.46, 25, 100), (659.26, 25, 100),
        (622.26, 25, 100), (659.26, 50, 400), (415.3, 25, 200),
        (554.36, 350, 100),
        (523.25, 250, 100), (493.88, 25, 100), (466.16, 25, 100),
        (440, 25, 100),
        (466.16, 50, 400), (311.13, 25, 200), (369.99, 350, 100),
        (311.13, 250, 100), (392, 25, 100), (466.16, 350, 100),
        (392, 250, 100),
        (466.16, 25, 100), (587.32, 700, 100), (784, 350, 100),
        (392, 250, 100),
        (392, 25, 100), (784, 350, 100), (739.98, 250, 100),
        (698.46, 25, 100),
        (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400),
        (415.3, 25, 200),
        (554.36, 350, 100), (523.25, 250, 100), (493.88, 25, 100),
        (466.16, 25, 100), (440, 25, 100), (466.16, 50, 400),
        (311.13, 25, 200),
        (392, 350, 100), (311.13, 250, 100), (466.16, 25, 100),
        (392.00, 300, 150), (311.13, 250, 100), (466.16, 25, 100), (392, 700)
    ])


def run_away(robot):
    time.sleep(3)
    robot.drive_system.go_straight_for_inches_using_encoder(10, 0 - 75)
    robot.drive_system.go(0 - 75, 75)
    time.sleep(1)
    robot.drive_system.stop()
    robot.drive_system.go_straight_for_inches_using_encoder(45, 100)
    robot.drive_system.stop()


def destroy(robot, speed):
    spin_then_pickup('cw', speed, robot)
    robot.drive_system.go_straight_for_seconds(2, 0 - speed)
    robot.arm_and_claw.lower_arm()
