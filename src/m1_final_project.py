"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Jacob Tebbe.
  Winter term, 2018-2019.
"""

import rosebot
import tkinter
import time
from tkinter import ttk

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
    pickup["command"] = lambda: sender.send_message('jacob_pick_up_object_beeping',[initial_beeping_rate, increasing_beeping_rate])

def pickup_object(initial_beeping, increasing_beeping,robot):
    initial_beeping = initial_beeping.get()
    increasing_beeping = increasing_beeping.get()
    print(initial_beeping, increasing_beeping)
    robot.go(50, 50)
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() > 7:
            if time.time() % initial_beeping == 0:
                robot.sound_system.beeper.beep().wait()
        elif robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() > = 3 :
            if time.time() % initial_beeping == 0:
                robot.sound_system.beeper.beep().wait()
        elif robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 3:
            break
    robot.stop()
