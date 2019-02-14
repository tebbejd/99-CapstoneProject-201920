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


def drive_encoder_frame(window, sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text='Driving Functions')
    frame_label.grid(row=0, column=1)
    # drive for seconds
    frame3_label = ttk.Label(frame, text='Go for Seconds')
    frame3_label.grid(row=1, column=0)
    drive_for_seconds = ttk.Button(frame, text="Drive for Seconds")
    speed_label = ttk.Label(frame, text="Speed (0 to 100)")
    speed_label.grid(row=2, column=0)
    seconds_label = ttk.Label(frame, text="Seconds")
    seconds_label.grid(row=4, column=0)
    speed_entry = ttk.Entry(frame, width=8)
    speed_entry.grid(row=3, column=0)
    drive_for_seconds.grid(row=6, column=0)
    seconds_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    seconds_entry.grid(row=5, column=0)
    drive_for_seconds["command"] = lambda: go_for_seconds(seconds_entry, sender, speed_entry)
    # drive for inches using time
    frame1_label = ttk.Label(frame, text="Go Inches Using Time")
    frame1_label.grid(row=1, column=1)
    drive_for_inches = ttk.Button(frame, text="Drive for Inches")
    speed1_label = ttk.Label(frame, text="Speed (0 to 100)")
    speed1_label.grid(row=2, column=1)
    inches_label = ttk.Label(frame, text="Inches")
    inches_label.grid(row=4, column=1)
    speed1_entry = ttk.Entry(frame, width=8)
    speed1_entry.grid(row=3, column=1)
    drive_for_inches.grid(row=6, column=1)
    inches_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    inches_entry.grid(row=5, column=1)
    drive_for_inches["command"] = lambda: go_for_inches_time(inches_entry, sender, speed1_entry)
    # drive for inches using encoder
    frame2_label = ttk.Label(frame, text="Go Inches Using Encoder")
    frame2_label.grid(row=1, column=2)
    drive1_for_inches = ttk.Button(frame, text="Drive for Inches")
    speed2_label = ttk.Label(frame, text="Speed (0 to 100)")
    speed2_label.grid(row=2, column=2)
    inches1_label = ttk.Label(frame, text="Inches")
    inches1_label.grid(row=4, column=2)
    speed2_entry = ttk.Entry(frame, width=8)
    speed2_entry.grid(row=3, column=2)
    drive1_for_inches.grid(row=6, column=2)
    inches1_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    inches1_entry.grid(row=5, column=2)
    drive1_for_inches["command"] = lambda: go_for_inches_encoder(inches1_entry, sender, speed2_entry)
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


def sound_frame(window, sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    frame_label = ttk.Label(frame, text='Sound System')
    frame_label.grid(row=0, column=1)
    # Construct the widgets on the frame:
    beep = ttk.Button(frame, text="Beep")
    number_of_beeps_label = ttk.Label(frame, text="Number of Beeps")
    number_of_beeps_label.grid(row=1, column=0)
    number_of_beeps = ttk.Entry(frame, width=8)
    number_of_beeps.grid(row=2, column=0)
    beep.grid(row=3, column=0)
    beep["command"] = lambda: beep_for_number(sender, number_of_beeps)
    # tone
    tone_button = ttk.Button(frame, text="Play Tone")
    frequency_label = ttk.Label(frame, text="Frequency")
    frequency_label.grid(row=3, column=1)
    duration_label = ttk.Label(frame, text="Duration(seconds)")
    duration_label.grid(row=1, column=1)
    tone_entry = ttk.Entry(frame, width=8)
    tone_entry.grid(row=4, column=1)
    tone_button.grid(row=5, column=1)
    duration_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    duration_entry.grid(row=2, column=1)
    tone_button["command"] = lambda: tone_at_given_frequency(tone_entry, sender, duration_entry)
    # phrase
    speak = ttk.Button(frame, text="Say Phrase")
    phrase_label = ttk.Label(frame, text="Phrase")
    phrase_label.grid(row=1, column=2)
    phrase = ttk.Entry(frame, width=16)
    phrase.grid(row=2, column=2)
    speak.grid(row=3, column=2)
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
    # Go forward
    go_for_distance = ttk.Button(frame, text="Go forward until distance")

    forward_label = ttk.Label(frame, text="How Close to object (inches)")
    forward_label.grid(row=0, column=0)
    forward_label1 = ttk.Label(frame, text="Inches")
    forward_label1.grid(row=1, column=0)
    close_to = ttk.Entry(frame, width=8)
    close_to.grid(row=2, column=0)
    forward_label2 = ttk.Label(frame, text="Speed")
    forward_label2.grid(row=3, column=0)
    speed_entry1 = ttk.Entry(frame, width=8)
    speed_entry1.grid(row=4, column=0)

    go_for_distance.grid(row=5, column=0)
    go_for_distance["command"] = lambda: go_forward_less_than(sender, close_to, speed_entry1)
    # Going backwards
    go_for_distance_backward = ttk.Button(frame, text="Go backward until distance")

    forward_label = ttk.Label(frame, text="How far from object (inches)")
    forward_label.grid(row=0, column=1)
    forward_label3 = ttk.Label(frame, text="Inches")
    forward_label3.grid(row=1, column=1)
    forward_label4 = ttk.Label(frame, text="Speed")
    forward_label4.grid(row=3, column=1)
    far_to = ttk.Entry(frame, width=8)
    far_to.grid(row=2, column=1)

    speed_entry2 = ttk.Entry(frame, width=8)
    speed_entry2.grid(row=4, column=1)

    go_for_distance_backward.grid(row=5, column=1)
    go_for_distance_backward["command"] = lambda: go_backward_greater_than(sender, far_to, speed_entry2)
    # Go for between
    go_for_distance_between = ttk.Button(frame, text="Go until between")

    forward_label = ttk.Label(frame, text="How Close to object (inches)")
    forward_label.grid(row=0, column=0)
    forward_label5 = ttk.Label(frame, text="Inches")
    forward_label5.grid(row=1, column=2)
    close_to_between = ttk.Entry(frame, width=8)
    close_to_between.grid(row=2, column=2)
    forward_label6 = ttk.Label(frame, text="Speed")
    forward_label6.grid(row=3, column=2)
    speed_entry3 = ttk.Entry(frame, width=8)
    speed_entry3.grid(row=4, column=2)
    forward_label7 = ttk.Label(frame, text="Delta")
    forward_label7.grid(row=5, column=2)
    delta = ttk.Entry(frame, width=8)
    delta.grid(row=6, column=2)

    go_for_distance_between.grid(row=7, column=2)
    go_for_distance_between["command"] = lambda: go_between(sender, close_to_between, delta, speed_entry3)
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


def get_color_sensor_frame(window, sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    # intensity less than
    frame_label = ttk.Label(frame, text="Color Sensor Operation")
    speed_label = ttk.Label(frame, text="Speed")
    intensity_label = ttk.Label(frame, text='Desired Intensity')
    speed_entry = ttk.Entry(frame, width=8)
    intensity_entry = ttk.Entry(frame, width=8)
    go_until_intensity = ttk.Button(frame, text="Go Until Intensity is Less")
    frame_label.grid(row=0, column=1)
    speed_label.grid(row=1, column=0)
    speed_entry.grid(row=2, column=0)
    intensity_label.grid(row=3, column=0)
    intensity_entry.grid(row=4, column=0)
    go_until_intensity.grid(row=5, column=0)
    go_until_intensity["command"] = lambda: go_until_intensity_less(sender, intensity_entry, speed_entry)
    # intensity greater than
    speed1_label = ttk.Label(frame, text="Speed")
    intensity1_label = ttk.Label(frame, text='Desired Intensity')
    speed_entry1 = ttk.Entry(frame, width=8)
    intensity_entry1 = ttk.Entry(frame, width=8)
    go_until_intensity_greater = ttk.Button(frame, text="Go Until Intensity is Greater")
    speed1_label.grid(row=1, column=1)
    speed_entry1.grid(row=2, column=1)
    intensity1_label.grid(row=3, column=1)
    intensity_entry1.grid(row=4, column=1)
    go_until_intensity_greater.grid(row=5, column=1)
    go_until_intensity_greater["command"] = lambda: go_until_intensity_greater_than(sender, intensity_entry1,
                                                                                    speed_entry1)
    # go until color is
    speed2_label = ttk.Label(frame, text="Speed")
    color_label = ttk.Label(frame, text='Desired Color Integer')
    color_name_label = ttk.Label(frame, text='Desired Color Name')
    speed2_entry = ttk.Entry(frame, width=8)
    color_entry = ttk.Entry(frame, width=8)
    color_name_entry = ttk.Entry(frame, width=8)
    go_until_color = ttk.Button(frame, text="Go Until Color Is")
    speed2_label.grid(row=1, column=2)
    speed2_entry.grid(row=2, column=2)
    color_label.grid(row=3, column=2)
    color_entry.grid(row=4, column=2)
    color_name_label.grid(row=5, column=2)
    color_name_entry.grid(row=6, column=2)
    go_until_color.grid(row=7, column=2)
    go_until_color["command"] = lambda: go_until_color_is(sender, color_name_entry, color_entry, speed2_entry)
    # go until color is not
    speed3_label = ttk.Label(frame, text="Speed")
    color1_label = ttk.Label(frame, text='Desired Color Integer')
    color1_name_label = ttk.Label(frame, text='Desired Color Name')
    speed3_entry = ttk.Entry(frame, width=8)
    color1_entry = ttk.Entry(frame, width=8)
    color1_name_entry = ttk.Entry(frame, width=8)
    go_until_color_not = ttk.Button(frame, text="Go Until Color Is Not")
    speed3_label.grid(row=1, column=3)
    speed3_entry.grid(row=2, column=3)
    color1_label.grid(row=3, column=3)
    color1_entry.grid(row=4, column=3)
    color1_name_label.grid(row=5, column=3)
    color1_name_entry.grid(row=6, column=3)
    go_until_color_not.grid(row=7, column=3)
    go_until_color_not["command"] = lambda: go_until_color_is_not(sender, color1_name_entry, color1_entry, speed3_entry)
    return frame


def get_camera_frame(window, sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()
    display_blob = ttk.Button(frame, text='Display Camera Data')
    display_blob.grid(row=1, column=0)
    display_blob["command"] = lambda: display_camera_data(sender)
    # intensity less than
    frame_label = ttk.Label(frame, text="Camera Operation")
    speed_label = ttk.Label(frame, text="Speed")
    area_label = ttk.Label(frame, text='Desired Area')
    speed_entry = ttk.Entry(frame, width=8)
    area_entry = ttk.Entry(frame, width=8)
    go_until_area = ttk.Button(frame, text="Spin to Find Object (CW)")
    frame_label.grid(row=0, column=1)
    speed_label.grid(row=1, column=1)
    speed_entry.grid(row=2, column=1)
    area_label.grid(row=3, column=1)
    area_entry.grid(row=4, column=1)
    go_until_area.grid(row=5, column=1)
    go_until_area["command"] = lambda: spin_clockwise(sender, area_entry, speed_entry)
    # intensity greater than
    speed1_label = ttk.Label(frame, text="Speed")
    area1_label = ttk.Label(frame, text='Desired Area')
    speed_entry1 = ttk.Entry(frame, width=8)
    area1_entry = ttk.Entry(frame, width=8)
    go_until_area1 = ttk.Button(frame, text="Spin to Find Object (CCW)")
    speed1_label.grid(row=1, column=2)
    speed_entry1.grid(row=2, column=2)
    area1_label.grid(row=3, column=2)
    area1_entry.grid(row=4, column=2)
    go_until_area1.grid(row=5, column=2)
    go_until_area1["command"] = lambda: spin_counterclockwise(sender, area1_entry, speed_entry1)
    return frame


def go_until_intensity_greater_than(sender, intensity, speed):
    intensity = intensity.get()
    speed = speed.get()
    print('Goes straight until the intensity is greater than', intensity, 'at speed', speed)
    sender.send_message('go_until_intensity_is_greater', [intensity, speed])


def go_until_intensity_less(sender, intensity, speed):
    intensity = intensity.get()
    speed = speed.get()
    print('Goes straight until the intensity is less than', intensity, 'at speed', speed)
    sender.send_message('go_until_intensity_is_less', [intensity, speed])


def go_until_color_is(sender, color_name, color, speed):
    color_name = color_name.get()
    color = color.get()
    speed = speed.get()
    print('Goes straight until the color is', color, color_name, 'at speed', speed)
    sender.send_message('go_until_color_is', [color, color_name, speed])


def go_until_color_is_not(sender, color_name, color, speed):
    color_name = color_name.get()
    color = color.get()
    speed = speed.get()
    print('Goes straight until the color is not', color, color_name, 'at speed', speed)
    sender.send_message('go_until_color_is_not', [color, color_name, speed])


def display_camera_data(sender):
    print('Display Camera Data')
    sender.send_message('display_camera_data')


def spin_clockwise(sender, area, speed):
    area = area.get()
    speed = speed.get()
    print('Spin clockwise until camera sees trained color with area', area, 'at speed', speed)
    sender.send_message('spin_clockwise_until_object', [area, speed])


def spin_counterclockwise(sender, area, speed):
    area = area.get()
    speed = speed.get()
    print('Spin counterclockwise until camera sees trained color with area', area, 'at speed', speed)
    sender.send_message('spin_counterclockwise_until_object', [area, speed])

