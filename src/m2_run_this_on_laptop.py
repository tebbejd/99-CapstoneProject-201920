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
    #frame1_2()
    sprint3()

def sprint3():
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
    root.title("RA Bot Controls")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # DONE: Implement and call get_my_frames(...)
    name_frame = get_name_frame(main_frame, mqtt_sender)
    control_frame = get_control_frame(main_frame, mqtt_sender)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames3(name_frame, control_frame)
    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()
def get_control_frame(window, sender):
    frame = ttk.Frame(window, padding=20, borderwidth=10, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="RA Duty")
    frame_label.grid()

    #Action 1 Quiet Hours
    quiet_hours = ttk.Button(frame, text="It's Quiet Hours")
    quiet_label = ttk.Label(frame, text="RA Bot Shouts It's Quiet Hours to let residence know")
    quiet_label.grid(row=0, column=2)
    quiet_hours.grid(row=0, column=0)
    quiet_hours["command"] = lambda: quiet_hours_func(sender, "It's Quiet Hours")

    #Action 2 Rounds
    rounds = ttk.Button(frame, text="Go on rounds")
    rounds_label = ttk.Label(frame, text="RA Bot needs to go on rounds")
    rounds_label.grid(row=2, column=2)
    rounds.grid(row=2, column=0)
    rounds_speed = ttk.Scale(frame, from_=30, to=100)
    rounds_speed.grid(row=2, column=1)
    rounds_speed_label = ttk.Label(frame, text="How Tired is RA Bot from awake to passed out")
    rounds_speed_label.grid(row=1, column=1)

    rounds["command"] = lambda: rounds_func(sender, rounds_speed)

    #Action 3 Floor Dinner
    floor_dinner = ttk.Button(frame, text="Floor Dinner")
    dinner_label = ttk.Label(frame, text="It's Saturday floor dinner")
    dinner_label.grid(row=4, column=2)
    floor_dinner.grid(row=4, column=0)
    var1 = tkinter.IntVar()
    location1 = ttk.Checkbutton(frame, text="Chavas", variable = var1)
    location1.grid(row=3, column=1)
    var2 = tkinter.IntVar()
    location2 = ttk.Checkbutton(frame, text="Royal", variable=var2)
    location2.grid(row=4, column=1)
    var3 = tkinter.IntVar()
    location3 = ttk.Checkbutton(frame, text="J-Gumbo's", variable=var3)
    location3.grid(row=5, column=1)
    floor_dinner["command"] = lambda: dinner_func(sender, var1, var2, var3)

    #Action 4 Dump beer (Inspection)


    #Action 5 Make fun of kids


    return frame

def dinner_func(sender, loc1, loc2, loc3):
    loc1 = int(loc1.get())
    loc2 = int(loc2.get())
    loc3 = int(loc3.get())
    if loc1 == 1:
        print("Chavas")
        sender.send_message('m2_floor_dinner', ["Chavas"])
    elif loc2 == 1:
        print("Royal")
        sender.send_message('m2_floor_dinner', ["Royal"])
    else:
        print("J-Gumbo's")
        sender.send_message('m2_floor_dinner', ["J-Gumbo's"])


def rounds_func(sender, speed):
    speed = speed.get()
    print(speed)
    sender.send_message('m2_rounds', [int(speed)])


def quiet_hours_func(sender, m):
    print(m)
    sender.send_message('m2_quiet_hours', [m])


def get_name_frame(window, sender):
    frame = ttk.Frame(window, padding=20, borderwidth=10, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="This is RA BOT")
    frame_label.grid()

    return frame
def grid_frames3(title_frame, control_frame):

    title_frame.grid(row = 0, column = 0)
    control_frame.grid(row = 1, column = 0)

def frame1_2():
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
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
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
    spin_frame = get_spin_frame(main_frame, mqtt_sender)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, tone_frame, spin_frame)
    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)


    return teleop_frame, arm_frame, control_frame

def grid_frames(teleop_frame, arm_frame, control_frame, tone_frame, spin_frame):
    teleop_frame.grid(row = 0, column = 0)
    arm_frame.grid(row = 1, column = 0)
    control_frame.grid(row = 2, column = 0)
    tone_frame.grid(row = 0, column = 1)
    spin_frame.grid(row = 1, column = 1)

def get_tone_frame(window, sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="Go using IR sensor")
    frame_label.grid()
    # Go forward
    go_for_distance = ttk.Button(frame, text="Approach")

    forward_label = ttk.Label(frame, text="Approach with tones")
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
    rate_label = ttk.Label(frame, text="Rate")
    rate_label.grid(row= 5, column = 0)
    rate.grid(row=6, column=0)

    go_for_distance.grid(row=7, column=0)
    go_for_distance["command"] = lambda: go_forward_tone(sender, initial, speed_entry1, rate)
    return frame

def go_forward_tone(sender, frequency, speed, rate):
    frequency = frequency.get()
    speed = speed.get()
    rate = rate.get()
    print(frequency, "HZ intial and", rate, "rate of increase")
    sender.send_message('m2_object_pickup_tone', [frequency, speed, rate])

def get_spin_frame(window, sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="Spin Pickup")
    frame_label.grid()
    # Clockwise
    go_for_distance = ttk.Button(frame, text="Clockwise")

    forward_label = ttk.Label(frame, text="Spin pickup")
    forward_label.grid(row=0, column=0)
    freq_label1 = ttk.Label(frame, text="Frequency")
    freq_label1.grid(row=1, column=0)
    initial = ttk.Entry(frame, width=8)
    initial.grid(row=2, column=0)
    speed_label2 = ttk.Label(frame, text="Speed")
    speed_label2.grid(row=3, column=0)
    speed_entry1 = ttk.Entry(frame, width=8)
    speed_entry1.grid(row=4, column=0)
    rate = ttk.Entry(frame, width=8)
    rate_label = ttk.Label(frame, text="Rate")
    rate_label.grid(row= 5, column = 0)
    rate.grid(row=6, column=0)

    go_for_distance.grid(row=7, column=0)
    go_for_distance["command"] = lambda: spin_pickup_clockwise(sender, initial, speed_entry1, rate)

    # Counter
    go_for_distance1 = ttk.Button(frame, text="Counter Clockwise")

    forward_label4 = ttk.Label(frame, text="Spin pickup")
    forward_label4.grid(row=0, column=1)
    freq_label5 = ttk.Label(frame, text="Frequency")
    freq_label5.grid(row=1, column=1)
    initial1 = ttk.Entry(frame, width=8)
    initial1.grid(row=2, column=1)
    speed_label6 = ttk.Label(frame, text="Speed")
    speed_label6.grid(row=3, column=1)
    speed_entry2 = ttk.Entry(frame, width=8)
    speed_entry2.grid(row=4, column=1)
    rate2 = ttk.Entry(frame, width=8)
    rate_label1 = ttk.Label(frame, text="Rate")
    rate_label1.grid(row=5, column=1)
    rate2.grid(row=6, column=1)

    go_for_distance1.grid(row=7, column=1)
    go_for_distance1["command"] = lambda: spin_pickup_counter(sender, initial1, speed_entry2, rate2)
    return frame

def spin_pickup_clockwise(sender, frequency, speed, rate):
    frequency = frequency.get()
    speed = speed.get()
    rate = rate.get()
    print(frequency, "HZ intial and", rate, "rate of increase")
    sender.send_message('brandon_spin_pickup', [frequency, speed, rate])

def spin_pickup_counter(sender, frequency, speed, rate):
    frequency = frequency.get()
    speed = speed.get()
    rate = rate.get()
    print(frequency, "HZ intial and", rate, "rate of increase")
    sender.send_message('brandon_spin_pickup_counterclockwise', [frequency, speed, rate])
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()