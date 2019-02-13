import mqtt_remote_method_calls as com
from tkinter import ttk
import shared_gui
import time
import math


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
    intial = ttk.Entry(frame, width=8)
    intial.grid(row=2, column=0)
    forward_label2 = ttk.Label(frame, text="Speed")
    forward_label2.grid(row=3, column=0)
    speed_entry1 = ttk.Entry(frame, width=8)
    speed_entry1.grid(row=4, column=0)
    rate = ttk.Entry(frame, width=8)
    rate.grid(row=5, column=0)

    go_for_distance.grid(row=6, column=0)
    go_for_distance["command"] = lambda: go_forward_tone(sender, intial, speed_entry1, rate)
    return frame

def go_forward_tone(sender, frequency, speed, rate):
    inches = frequency.get()
    speed = speed.get()
    rate = rate.get()
    print(frequency, "HZ intial and", rate, "rate of increase")
    sender.send_message('go_forward_tone', [frequency, speed, rate])

def pickup_object_tone(frequency, speed, rate, robot):
    robot.go(speed, speed)
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 2:
            break
        robot.sound_system.tone_maker.play_tone(frequency, rate)