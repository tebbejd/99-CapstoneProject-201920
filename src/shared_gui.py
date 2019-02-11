"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Jacob Tebbe and Brandon Wohlfarth.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame


###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    left_entry_box = left_entry_box.get()
    right_entry_box = right_entry_box.get()
    print('forward', left_entry_box, right_entry_box)
    mqtt_sender.send_message('forward', [left_entry_box, right_entry_box])


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    left_entry_box = left_entry_box.get()
    right_entry_box = right_entry_box.get()
    print('backward', left_entry_box, right_entry_box)
    mqtt_sender.send_message('backward', [left_entry_box, right_entry_box])


def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    left_entry_box = left_entry_box.get()
    right_entry_box = right_entry_box.get()
    print('left', left_entry_box, right_entry_box)
    mqtt_sender.send_message('left', [left_entry_box, right_entry_box])


def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    left_entry_box = left_entry_box.get()
    right_entry_box = right_entry_box.get()
    print('right', left_entry_box, right_entry_box)
    mqtt_sender.send_message('right', [left_entry_box, right_entry_box])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print('stop')
    mqtt_sender.send_message('stop')


###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print('raise arm')
    mqtt_sender.send_message('raise_arm')


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print('lower arm')
    mqtt_sender.send_message('lower_arm')


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print('calibrate arm')
    mqtt_sender.send_message('calibrate_arm')


def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    arm_position_entry = arm_position_entry.get()
    print('move arm to position', arm_position_entry)
    mqtt_sender.send_message('arm_to_position', [arm_position_entry])


###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('End code for robot')
    mqtt_sender.send_message('quit')
    print('Robot code has been terminated')


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print('End code for robot')
    mqtt_sender.send_message('quit')
    print('Robot code has been terminated')
    print('Now exit the remote control')
    exit()


def get_seconds_frame(window, sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    drive_for_seconds = ttk.Button(frame, text="Drive for Seconds")
    # Grid the widgets:
    speed_label = ttk.Label(frame, text="Speed (0 to 100)")
    speed_label.grid(row=0, column=0)

    seconds_label = ttk.Label(frame, text="Seconds")
    seconds_label.grid(row=0, column=1)

    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.grid(row=1, column=0)

    drive_for_seconds.grid(row=2, column=1)
    seconds_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    seconds_entry.grid(row=1, column=1)
    drive_for_seconds["command"] = lambda: go_for_seconds(seconds_entry, sender, speed_entry)
    return frame


def get_inches_time_frame(window, sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="Go Inches Using Time")
    frame_label.grid()
    # Construct the widgets on the frame:
    drive_for_inches = ttk.Button(frame, text="Drive for Inches")

    speed_label = ttk.Label(frame, text="Speed (0 to 100)")
    speed_label.grid(row=1, column=0)

    inches_label = ttk.Label(frame, text="Inches")
    inches_label.grid(row=1, column=1)

    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.grid(row=2, column=0)

    drive_for_inches.grid(row=3, column=1)
    inches_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    inches_entry.grid(row=2, column=1)
    drive_for_inches["command"] = lambda: go_for_inches_time(inches_entry, sender, speed_entry)
    return frame


def get_inches_encoder_frame(window, sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="Go Inches Using Encoder")
    frame_label.grid()

    # Construct the widgets on the frame:
    drive_for_inches = ttk.Button(frame, text="Drive for Inches")

    speed_label = ttk.Label(frame, text="Speed (0 to 100)")
    speed_label.grid(row=1, column=0)

    inches_label = ttk.Label(frame, text="Inches")
    inches_label.grid(row=1, column=1)

    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.grid(row=2, column=0)

    drive_for_inches.grid(row=3, column=1)
    inches_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    inches_entry.grid(row=2, column=1)
    drive_for_inches["command"] = lambda: go_for_inches_encoder(inches_entry, sender, speed_entry)
    return frame


def go_for_seconds(box, sender, speed):
    box = box.get()
    speed = speed.get()
    print('go straight for', box, 'seconds ', 'at speed', speed)
    sender.send_message('go_straight_for_seconds', [box, speed])


def go_for_inches_time(box, sender, speed):
    box = box.get()
    speed = speed.get()
    print('go straight for', box, 'inches ', 'at speed', speed)
    sender.send_message('go_straight_for_inches_using_time', [box, speed])


def go_for_inches_encoder(box, sender, speed):
    box = box.get()
    speed = speed.get()
    print('go straight for', box, 'inches', 'at speed', speed)
    sender.send_message('go_straight_for_inches_using_encoder', [box, speed])


def get_beep_frame(window, sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    beep = ttk.Button(frame, text="Beep")

    number_of_beeps_label = ttk.Label(frame, text="Number of Beeps")
    number_of_beeps_label.grid(row=0, column=0)

    number_of_beeps = ttk.Entry(frame, width=8)
    number_of_beeps.grid(row=1, column=0)

    beep.grid(row=2, column=0)
    beep["command"] = lambda: beep_for_number(sender, number_of_beeps)
    return frame


def get_tone_frame(window, sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    tone_button = ttk.Button(frame, text="Play Tone")

    frequency_label = ttk.Label(frame, text="Frequency")
    frequency_label.grid(row=0, column=1)

    duration_label = ttk.Label(frame, text="Duration(seconds)")
    duration_label.grid(row=0, column=0)

    tone_entry = ttk.Entry(frame, width=8)
    tone_entry.grid(row=1, column=1)

    tone_button.grid(row=2, column=1)
    duration_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    duration_entry.grid(row=1, column=0)
    tone_button["command"] = lambda: tone_at_given_frequency(tone_entry, sender, duration_entry)
    return frame


def get_phrase_frame(window, sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    speak = ttk.Button(frame, text="Say Phrase")

    phrase_label = ttk.Label(frame, text="Phrase")
    phrase_label.grid(row=0, column=0)

    phrase = ttk.Entry(frame, width=8)
    phrase.grid(row=1, column=0)

    speak.grid(row=2, column=0)
    speak["command"] = lambda: speak_phrase(sender, phrase)
    return frame


def beep_for_number(sender, number):
    number = number.get()
    print('beep', number, 'times')
    sender.send_message('beep_for_given_number', [number])


def tone_at_given_frequency(tone, sender, duration):
    tone = tone.get()
    duration = duration.get()
    print('frequency is', tone, 'Plays for', duration, 'seconds')
    sender.send_message('tone_at_a_given_frequency', [tone, duration])


def speak_phrase(sender, phrase):
    phrase = phrase.get()
    print('speak', phrase)
    sender.send_message('speak_phrase', [phrase])

def get_IR_frame(window, sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text="Go using IR sensor")
    frame_label.grid()

    go_for_distance = ttk.Button(frame, text="Go forward until distance")

    forward_label = ttk.Label(frame, text="How Close to object (inches)")
    forward_label.grid(row=0, column=0)

    close_to = ttk.Entry(frame, width=8)
    close_to.grid(row=1, column=0)
    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.grid(row=2, column=0)

    go_for_distance.grid(row=3, column=0)
    go_for_distance["command"] = lambda: go_forward_less_than(sender, close_to, speed_entry)

    go_for_distance_backward = ttk.Button(frame, text="Go backward until distance")

    forward_label = ttk.Label(frame, text="How far from object (inches)")
    forward_label.grid(row=0, column=1)

    far_to = ttk.Entry(frame, width=8)
    far_to.grid(row=1, column=1)

    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.grid(row=2, column=1)

    go_for_distance_backward.grid(row=3, column=1)
    go_for_distance_backward["command"] = lambda: go_backward_greater_than(sender, far_to, speed_entry)

    go_for_distance_between = ttk.Button(frame, text="Go until between")

    forward_label = ttk.Label(frame, text="Distance from object (inches)")
    forward_label.grid(row=0, column=2)

    close_to = ttk.Entry(frame, width=8)
    close_to.grid(row=1, column=2)

    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.grid(row=2, column=2)

    delta = ttk.Entry(frame, width=8)
    delta.grid(row=3, column=2)

    go_for_distance_between.grid(row=2, column=2)
    go_for_distance_between["command"] = lambda: go_between(sender, close_to, delta, speed_entry)
    return frame

def go_forward_less_than(sender, inches, speed):
    inches = inches.get()
    speed = speed.get()
    print(inches, "Away from object")
    sender.send_message('go_forward_until_distance_is_less_than', [inches, speed])

def go_backward_greater_than(sender, inches, speed):
    inches = inches.get()
    speed = speed.get()
    print(inches, "Away from object")
    sender.send_message('go_backward_until_distance_is_greater_than', [inches, speed])

def go_between(sender, inches, delta, speed):
    inches = inches.get()
    speed = speed.get()
    delta = delta.get()
    print(inches, "Away from object (between)")
    sender.send_message('go_until_distance_is_within', [inches, delta, speed])