"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Jacob Tebbe and Brandon Wohlfarth.
  Winter term, 2018-2019.
"""


class DelegateThatReceives(object):

    def __init__(self, robot):
        """" :type robot:  rosebot.RoseBot """
        self.robot = robot
        self.is_time_to_stop = False

    def forward(self, left_wheel, right_wheel):
        self.robot.drive_system.go(int(left_wheel), int(right_wheel))
        print('forward')

    def backward(self, left_wheel, right_wheel):
        self.robot.drive_system.go(0 - int(left_wheel), 0 - int(right_wheel))
        print('backward')

    def left(self, left_wheel, right_wheel):
        self.robot.drive_system.go(0 - int(left_wheel), int(right_wheel))
        print('left')

    def right(self, left_wheel, right_wheel):
        self.robot.drive_system.go(int(left_wheel), 0 - int(right_wheel))
        print('right')

    def stop(self):
        self.robot.drive_system.stop()
        print('STOP!!!')

    def raise_arm(self):
        self.robot.arm_and_claw.raise_arm()
        print('raise arm')

    def lower_arm(self):
        self.robot.arm_and_claw.lower_arm()
        print('lower arm')

    def calibrate_arm(self):
        self.robot.arm_and_claw.calibrate_arm()
        print('calibrate')

    def arm_to_position(self, pos):
        self.robot.arm_and_claw.move_arm_to_position(int(pos))
        print('arm position')

    def go_straight_for_seconds(self, time, left_wheel):
        self.robot.drive_system.go_straight_for_seconds(int(time), int(left_wheel))
        print('strait for seconds')

    def go_straight_for_inches_using_time(self, inches, left_wheel):
        self.robot.drive_system.go_straight_for_inches_using_time(int(inches), int(left_wheel))
        print('strait for inches using time')

    def go_straight_for_inches_using_encoder(self, inches, left_wheel):
        self.robot.drive_system.go_straight_for_inches_using_encoder(int(inches), int(left_wheel))
        print('strait for inches using distance')

    def beep_for_given_number(self, number):
        print('I will beep', number, 'times')
        for k in range(int(number)):
            self.robot.sound_system.beeper.beep().wait()

    def tone_at_a_given_frequency(self, tone, duration):
        print('I will play a tone at frequency', tone, 'for duration', duration)
        self.robot.sound_system.tone_maker.play_tone(int(tone), int(duration) * 1000)

    def speak_phrase(self, phrase):
        print('I will speak phrase', phrase)
        self.robot.sound_system.speech_maker.speak(phrase)

    def quit(self):
        self.is_time_to_stop = True

    def go_forward_until_distance_is_less_than(self, close_to, speed):
        print("Go forward until", close_to, "inches away from object")
        self.robot.drive_system.go_forward_until_distance_is_less_than(int(close_to), int(speed))

    def go_backward_until_distance_is_greater_than(self, inches, speed):
        print("Go backwards until", inches, "inches away from object")
        self.robot.drive_system.go_backward_until_distance_is_greater_than(int(inches), int(speed))

    def go_until_distance_is_within(self, inches, delta, speed):
        print("Go until", inches, "inches from object")
        self.robot.drive_system.go_until_distance_is_within(int(delta), int(inches), int(speed))

    def go_until_intensity_is_greater(self, intensity, speed):
        print('Goes straight until the intensity is greater than', intensity, 'at speed', speed)
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(int(intensity), int(speed))

    def go_until_intensity_is_less(self, intensity, speed):
        print('Goes straight until the intensity is less than', intensity, 'at speed', speed)
        self.robot.drive_system.go_straight_until_intensity_is_less_than(int(intensity), int(speed))

    def go_until_color_is(self, color_int, color_name, speed):
        if color_int is None:
            color = color_name
        else:
            color = int(color_int)
        print('Goes straight until the color is', color, 'at speed', speed)
        self.robot.drive_system.go_straight_until_color_is(color, int(speed))

    def go_until_color_is_not(self, color_int, color_name, speed):
        if color_name is '':
            color = int(color_int)
        else:
            color = color_name
        print('Goes straight until the color is not', color, 'at speed', speed)
        self.robot.drive_system.go_straight_until_color_is_not(color, int(speed))

    def display_camera_data(self):
        print('display camera data')
        self.robot.drive_system.display_camera_data()

    def spin_clockwise_until_object(self, speed, area):
        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed), int(area))

    def spin_counterclockwise_until_object(self, speed, area):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), int(area))
