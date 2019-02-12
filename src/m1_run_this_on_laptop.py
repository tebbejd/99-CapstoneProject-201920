"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Jacob Tebbe.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    sender = com.MqttClient()
    sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title('Capstone Project Winter 2019')

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    frame.grid()
    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame = get_shared_frames(frame, sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DONE: Implement and call get_my_frames(...)
    get_my_frames(frame, sender)
    grid_color_sensor_frames(frame, sender)
    grid_camera_frames(frame, sender)
    grid_proximity_sensor(frame, sender)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)

    return teleop_frame, arm_frame, control_frame


def grid_frames(teleop_frame, arm_frame, control_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)


def get_my_frames(frame, sender):
    go_straight_for_seconds = shared_gui.get_seconds_frame(frame, sender)
    go_straight_for_inches_timed = shared_gui.get_inches_time_frame(frame, sender)
    go_straight_for_inches_encoder = shared_gui.get_inches_encoder_frame(frame, sender)
    beep_for_given_number = shared_gui.get_beep_frame(frame, sender)
    play_tone_at_frequency = shared_gui.get_tone_frame(frame, sender)
    speak_phrase = shared_gui.get_phrase_frame(frame, sender)

    grid_my_frames(go_straight_for_seconds, go_straight_for_inches_timed, go_straight_for_inches_encoder,
                   beep_for_given_number, play_tone_at_frequency, speak_phrase)


def grid_my_frames(go_straight_for_seconds, go_straight_for_inches_timed, go_straight_for_inches_encoder,
                   beep_for_given_number, play_tone_at_frequency, speak_phrase):
    go_straight_for_seconds.grid(row=0, column=1)
    go_straight_for_inches_timed.grid(row=1, column=1)
    go_straight_for_inches_encoder.grid(row=2, column=1)
    beep_for_given_number.grid(row=0, column=2)
    play_tone_at_frequency.grid(row=1, column=2)
    speak_phrase.grid(row=2, column=2)


def grid_color_sensor_frames(frame, sender):
    color_sensor_frame = shared_gui.get_color_sensor_frame(frame, sender)
    color_sensor_frame.grid(row=0, column=3)
    pass


def grid_proximity_sensor(frame, sender):
    proximity_frame = shared_gui.get_IR_frame(frame, sender)
    proximity_frame.grid(row=1, column=3)


def grid_camera_frames(frame, sender):
    camera_frame = shared_gui.get_camera_frame(frame, sender)
    camera_frame.grid(row=2, column=3)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
