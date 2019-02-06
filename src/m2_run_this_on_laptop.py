"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Brandon Wohlfarth.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui
import time
import math

def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")

    mqtt_client = com.MqttClient()
    mqtt_client.connect(name1, name2)
    time.sleep(1)

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------


    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------


    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------


    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------


    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------



def get_shared_frames(main_frame, mqtt_sender):
    pass


def grid_frames(teleop_frame, arm_frame, control_frame):
    pass


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()