import pyautogui
from handmodel import Gesture
import time
import os
import osascript

from . import hand_shake
from . import music
from . import presentation
from . import reading


def swipe_left():
    pyautogui.hotkey('ctrl', 'right')
    return action_profile


def swipe_right():
    pyautogui.hotkey('ctrl', 'left')
    return action_profile


def swipe_up():
    pyautogui.hotkey('ctrl', 'up')
    return action_profile


def swipe_down():
    pyautogui.hotkey('ctrl', 'down')
    return action_profile


def two_finger_up():
    for i in range(10):
        pyautogui.scroll(-2)
    return action_profile


def two_finger_down():
    for i in range(10):
        pyautogui.scroll(2)
    return action_profile


def two_finger_right():
    for i in range(10):
        pyautogui.hscroll(-2)
    return action_profile


def two_finger_left():
    for i in range(10):
        pyautogui.hscroll(2)
    return action_profile


def two_finger_away():
    return action_profile


def two_finger_in():
    return action_profile


def rolling_hand_forward():
    print('Dimming')
    os.system('brightness 0.5')
    return reading.action_profile


def rolling_hand_backward():
    return action_profile


def turning_hand_clockwise():
    pyautogui.hotkey('command', 'tab')
    return action_profile


def turning_hand_cclockwise():
    pyautogui.hotkey('command', 'shift', 'tab')
    return action_profile


def zooming_in_full_hand():
    pyautogui.hotkey('command', '+')
    return action_profile


def zooming_out_full_hand():
    pyautogui.hotkey('command', '-')
    return action_profile


def zooming_in_two_fingers():
    return action_profile


def zooming_out_two_fingers():
    return action_profile


def pushing_hand_away():
    pyautogui.hotkey('f11')
    return action_profile


def pulling_hand_in():
    pyautogui.hotkey('f12')
    return action_profile


def thumb_up():
    return action_profile


def thumb_down():
    return action_profile


def shaking_hand():
    pyautogui.keyDown('command')
    pyautogui.press('tab')
    return hand_shake.action_profile


def stop_sign():
    pyautogui.hotkey('command', 'enter')
    return presentation.action_profile


def drumming_fingers():
    title = 'Music Control'
    text = 'Switching to Music Controls'
    os.system("""osascript -e 'display notification "{}" with title "{}"'
                  """.format(text, title))
    return music.action_profile


action_profile = {
    Gesture.SwipingLeft: swipe_left,
    Gesture.SwipingRight: swipe_right,
    Gesture.SwipingDown: swipe_down,
    Gesture.SwipingUp: swipe_up,
    Gesture.PushingHandAway: pushing_hand_away,
    Gesture.PullingHandIn: pulling_hand_in,
    Gesture.SlidingTwoFingersLeft: two_finger_left,
    Gesture.SlidingTwoFingersRight: two_finger_right,
    Gesture.SlidingTwoFingersDown: two_finger_down,
    Gesture.SlidingTwoFingersUp: two_finger_up,
    Gesture.PushingTwoFingersAway: two_finger_away,
    Gesture.PullingTwoFingersIn: two_finger_in,
    Gesture.RollingHandForward: rolling_hand_forward,
    Gesture.RollingHandBackward: rolling_hand_backward,
    Gesture.TurningHandClockwise: turning_hand_clockwise,
    Gesture.TurningHandCounterclockwise: turning_hand_cclockwise,
    Gesture.ZoomingInWithFullHand: zooming_in_full_hand,
    Gesture.ZoomingOutWithFullHand: zooming_out_full_hand,
    Gesture.ZoomingInWithTwoFingers: zooming_in_two_fingers,
    Gesture.ZoomingOutWithTwoFingers: zooming_out_two_fingers,
    Gesture.ThumbUp: thumb_up,
    Gesture.ThumbDown: thumb_down,
    Gesture.ShakingHand: shaking_hand,
    Gesture.StopSign: stop_sign,
    Gesture.DrummingFingers: drumming_fingers,
    Gesture.NoGesture: lambda: action_profile,
    Gesture.DoingOtherThings: lambda: action_profile,
}
