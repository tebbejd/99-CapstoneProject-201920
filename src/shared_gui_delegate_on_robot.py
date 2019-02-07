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

    def backward(self,left_wheel, right_wheel):
        self.robot.drive_system.go(0-int(left_wheel), 0-int(right_wheel))

    def left(self, left_wheel, right_wheel):
        self.robot.drive_system.go(0-int(left_wheel), int(right_wheel))

    def right(self, left_wheel, right_wheel):
        self.robot.drive_system.go(int(left_wheel), 0-int(right_wheel))

    def stop(self):
        self.robot.drive_system.stop()

    def raise_arm(self):
        self.robot.ArmAndClaw.raise_arm()

    def lower_arm(self):
        self.robot.ArmAndClaw.lower_arm()

    def calibrate_arm(self):
        self.robot.ArmAndClaw.calibrate_arm()

    def arm_to_position(self, pos):
        self.robot.ArmAndClaw.move_arm_to_position(pos)
        
