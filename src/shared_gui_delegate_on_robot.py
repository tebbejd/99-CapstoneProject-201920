"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Jacob Tebbe and Brandon Wohlfarth.
  Winter term, 2018-2019.
"""
import m1_final_project as jacob
import m2_extra as brandon


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
        if color_int is '':
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

    def spin_clockwise_until_object(self, area, speed):
        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed), int(area))

    def spin_counterclockwise_until_object(self, area, speed):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), int(area))

    def jacob_pick_up_object_beeping(self, initial_beeping, increasing_beeping):
        print(initial_beeping, increasing_beeping)
        jacob.pickup_object_beep(initial_beeping, increasing_beeping, self.robot)

    def m2_object_pickup_tone(self, frequency, speed, rate):
        brandon.pickup_object_tone(float(frequency), int(speed), float(rate), self.robot)

    def jacob_pick_up_object_leds(self, initial_cycle, increasing_cycle):
        print(initial_cycle, increasing_cycle)
        jacob.pickup_object_leds(initial_cycle, increasing_cycle, self.robot)

    def jacob_spin_pickup(self, speed, direction):
        print(direction)
        jacob.spin_then_pickup(direction, int(speed), self.robot)

    def jacob_spin_pickup_leds(self, speed, direction):
        print(direction)
        jacob.spin_then_pickup_leds(direction, int(speed), self.robot)

    def brandon_spin_pickup(self, frequency, speed, rate):
        brandon.spin_pickup_clockwise(float(frequency), int(speed), float(rate), self.robot)

    def brandon_spin_pickup_counterclockwise(self, frequency, speed, rate):
        brandon.spin_pickup_counterclockwise(float(frequency), int(speed), float(rate), self.robot)

    def m1_end_of_desruction_bot(self):
        phrase = 'My time has come. I hope I was a good boy.'
        self.speak_phrase(phrase)

    def m1_survey_the_site(self):
        pass

    def m1_head_towards_site(self):
        pass

    def m1_start_destruction(self,answer, speed):
        answer = answer.get()
        if answer == 'yes':
            print('My speed is set to', speed)
        else:
            print('I will wait until you are ready')
            return