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
            self.robot.beeper.beep()

    def tone_at_a_given_frequency(self, tone, duration):
        print('I will play a tone at frequency', tone, 'for duration', duration)
        self.robot.tone_maker.tone(int(tone), int(duration))

    def speak_phrase(self, phrase):
        print('I will speak phrase', phrase)
        self.robot.speech_maker.speak(phrase)

    def quit(self):
        exit()