"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Brandon Wohlfarth.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    #run_test_arm()
    real_thing()

def run_test_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()
    robot.arm_and_claw.raise_arm()
    #time.sleep(0.1)
    robot.arm_and_claw.lower_arm()
    #time.sleep(0.1)
    robot.arm_and_claw.calibrate_arm()
    #time.sleep(0.1)
    robot.arm_and_claw.move_arm_to_position(2500)
    #time.sleep(0.1)

def real_thing():
    robot = rosebot.RoseBot()
    delagate_That_Receives = shared_gui_delegate_on_robot.DelagateThatReceives(robot)
    mqtt_reciever = com.MqttClient(delagate_That_Receives)
    mqtt_reciever.connect_to_pc()

    while True:
        time.sleep(0.01)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()