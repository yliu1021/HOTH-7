import pyautogui
from handmodel import Gesture

from . import default


def swipe_left():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def swipe_right():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def swipe_up():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def swipe_down():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def two_finger_up():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def two_finger_down():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def two_finger_right():
    pyautogui.press('right')
    return action_profile


def two_finger_left():
    pyautogui.press('left')
    return action_profile


def two_finger_away():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def two_finger_in():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def rolling_hand_forward():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def rolling_hand_backward():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def turning_hand_clockwise():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def turning_hand_cclockwise():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def zooming_in_full_hand():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def zooming_out_full_hand():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def zooming_in_two_fingers():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def zooming_out_two_fingers():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def pushing_hand_away():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def pulling_hand_in():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def thumb_up():
    pyautogui.keyUp('command')
    return default.action_profile


def thumb_down():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def shaking_hand():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def stop_sign():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


def drumming_fingers():
    pyautogui.press('esc')
    pyautogui.keyUp('command')
    return default.action_profile


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
