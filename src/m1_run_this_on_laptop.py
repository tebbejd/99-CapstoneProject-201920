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
import m1_final_project as me

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
    pickup_object_using_proximity_sensor(frame,sender).grid(row=3,column=0)
    spin_pickup_object(frame,sender).grid(row=3,column=1)

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
    driving_frame = shared_gui.drive_encoder_frame(frame, sender)
    sound_frame = shared_gui.sound_frame(frame, sender)
    grid_my_frames(sound_frame, driving_frame)


def grid_my_frames(sound_frame, driving_frame):
    sound_frame.grid(row=1, column=1)
    driving_frame.grid(row=0, column=1)


def grid_color_sensor_frames(frame, sender):
    color_sensor_frame = shared_gui.get_color_sensor_frame(frame, sender)
    color_sensor_frame.grid(row=0, column=2)



def grid_proximity_sensor(frame, sender):
    proximity_frame = shared_gui.get_IR_frame(frame, sender)
    proximity_frame.grid(row=1, column=2)


def grid_camera_frames(frame, sender):
    camera_frame = shared_gui.get_camera_frame(frame, sender)
    camera_frame.grid(row=2, column=2)

def pickup_object_using_proximity_sensor(window,sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid(row=3, column=0)
    frame_label = ttk.Label(frame, text='Pickup object using Proximity Sensor')
    frame_label.grid(row=0, column=0)
    initial_beeping_rate = ttk.Entry(frame, width=8)
    increasing_beeping_rate = ttk.Entry(frame, width=8)
    initial_label = ttk.Label(frame, text='Initial Beeping rate')
    increasing_label = ttk.Label(frame, text='Increasing Beeping rate')
    pickup = ttk.Button(frame, text='Pickup object')
    initial_label.grid(row=1, column=0)
    initial_beeping_rate.grid(row=2, column=0)
    increasing_label.grid(row=3, column=0)
    increasing_beeping_rate.grid(row=4, column=0)
    pickup.grid(row=5, column=0)
    pickup["command"] = lambda: sender.send_message('jacob_pick_up_object_beeping',[initial_beeping_rate.get(), increasing_beeping_rate.get()])
    #leds
    initial_cycle_rate = ttk.Entry(frame, width=8)
    increasing_cycle_rate = ttk.Entry(frame, width=8)
    initial_label = ttk.Label(frame, text='Initial Cycle Rate')
    increasing_label = ttk.Label(frame, text='Increasing Cycle Rate')
    pickup1 = ttk.Button(frame, text='Pickup object')
    initial_label.grid(row=1, column=1)
    initial_cycle_rate.grid(row=2, column=1)
    increasing_label.grid(row=3, column=1)
    increasing_cycle_rate.grid(row=4, column=1)
    pickup1.grid(row=5, column=1)
    pickup1["command"] = lambda: sender.send_message('jacob_pick_up_object_leds',[initial_cycle_rate.get(), increasing_cycle_rate.get()])
    return frame

def spin_pickup_object(window,sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid(row=3, column=1)
    frame_label = ttk.Label(frame, text='Spin Then Pickup while Beeping')
    frame_label.grid(row=0, column=0)
    direction = ttk.Entry(frame, width=8)
    speed = ttk.Entry(frame, width=8)
    direction_label = ttk.Label(frame, text='Spin Direction CW or CCW')
    speed_of_spin_label = ttk.Label(frame, text='Speed of Spin')
    pickup = ttk.Button(frame, text='Pickup object')
    direction_label.grid(row=1, column=0)
    direction.grid(row=2, column=0)
    speed_of_spin_label.grid(row=3, column=0)
    speed.grid(row=4, column=0)
    pickup.grid(row=5, column=0)
    pickup["command"] = lambda: sender.send_message('jacob_spin_pickup',[speed.get(), direction.get()])
    #leds
    frame1 = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame1.grid(row=3, column=1)
    frame1_label = ttk.Label(frame, text='Spin Then Pickup while Leds flash')
    frame1_label.grid(row=0, column=1)
    direction1 = ttk.Entry(frame, width=8)
    speed1 = ttk.Entry(frame, width=8)
    direction1_label = ttk.Label(frame, text='Spin Direction CW or CCW')
    speed1_of_spin_label = ttk.Label(frame, text='Speed of Spin')
    pickup1 = ttk.Button(frame, text='Pickup object')
    direction1_label.grid(row=1, column=1)
    direction1.grid(row=2, column=1)
    speed1_of_spin_label.grid(row=3, column=1)
    speed1.grid(row=4, column=1)
    pickup1.grid(row=5, column=1)
    pickup1["command"] = lambda: sender.send_message('jacob_spin_pickup_leds', [speed1.get(), direction1.get()])
    return frame




# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
