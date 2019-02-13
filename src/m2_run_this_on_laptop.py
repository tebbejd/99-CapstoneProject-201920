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
import m2_extra as brandon

def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()


    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE Capstone Porject 2019")


    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding = 10, borderwidth =5, relief = "groove")
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)
    tone_frame = get_tone_frame(main_frame, mqtt_sender)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, tone_frame)
    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)


    return teleop_frame, arm_frame, control_frame

def grid_frames(teleop_frame, arm_frame, control_frame, tone_frame):
    teleop_frame.grid(row = 0, column = 0)
    arm_frame.grid(row = 1, column = 0)
    control_frame.grid(row = 2, column = 0)
    tone_frame.grid(row = 0, column = 1)

def get_tone_frame(window, sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="Go using IR sensor")
    frame_label.grid()
    # Go forward
    go_for_distance = ttk.Button(frame, text="Go forward until distance")

    forward_label = ttk.Label(frame, text="How Close to object (inches)")
    forward_label.grid(row=0, column=0)
    forward_label1 = ttk.Label(frame, text="Frequency")
    forward_label1.grid(row=1, column=0)
    initial = ttk.Entry(frame, width=8)
    initial.grid(row=2, column=0)
    forward_label2 = ttk.Label(frame, text="Speed")
    forward_label2.grid(row=3, column=0)
    speed_entry1 = ttk.Entry(frame, width=8)
    speed_entry1.grid(row=4, column=0)
    rate = ttk.Entry(frame, width=8)
    rate.grid(row=5, column=0)

    go_for_distance.grid(row=6, column=0)
    go_for_distance["command"] = lambda: go_forward_tone(sender, initial, speed_entry1, rate)
    return frame

def go_forward_tone(sender, frequency, speed, rate):
    frequency = frequency.get()
    speed = speed.get()
    rate = rate.get()
    print(frequency, "HZ intial and", rate, "rate of increase")
    sender.send_message('m2_object_pickup_tone', [frequency, speed, rate])




# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()