import pyautogui
from handmodel import Gesture
import os
import osascript

from . import default


def switch_back():
    title = 'Music Control'
    text = 'Switching to Music Controls'
    os.system("""osascript -e 'display notification "{}" with title "{}"'""".format(text, title))


def swipe_left():
    switch_back()
    return default.action_profile


def swipe_right():
    switch_back()
    return default.action_profile


def swipe_up():
    switch_back()
    return default.action_profile


def swipe_down():
    switch_back()
    return default.action_profile


def two_finger_up():
    _, o, _ = osascript.run('get volume settings')
    v = int(o.split(',')[0].split(':')[1]) # pray
    v += 10
    osascript.run(f'set volume output volume {v}')
    return action_profile


def two_finger_down():
    _, o, _ = osascript.run('get volume settings')
    v = int(o.split(',')[0].split(':')[1])  # pray
    v -= 10
    osascript.run(f'set volume output volume {v}')
    return action_profile


def two_finger_right():
    osascript.run("""tell application "Music"
                        next track
                    end tell""")
    return action_profile


def two_finger_left():
    osascript.run("""tell application "Music"
                        previous track
                    end tell""")
    return action_profile


def two_finger_away():
    switch_back()
    return default.action_profile


def two_finger_in():
    switch_back()
    return default.action_profile


def rolling_hand_forward():
    switch_back()
    return default.action_profile


def rolling_hand_backward():
    switch_back()
    return default.action_profile


def turning_hand_clockwise():
    switch_back()
    return default.action_profile


def turning_hand_cclockwise():
    switch_back()
    return default.action_profile


def zooming_in_full_hand():
    switch_back()
    return default.action_profile


def zooming_out_full_hand():
    switch_back()
    return default.action_profile


def zooming_in_two_fingers():
    switch_back()
    return default.action_profile


def zooming_out_two_fingers():
    switch_back()
    return default.action_profile


def pushing_hand_away():
    switch_back()
    return default.action_profile


def pulling_hand_in():
    switch_back()
    return default.action_profile


def thumb_up():
    switch_back()
    return default.action_profile


def thumb_down():
    switch_back()
    return default.action_profile


def shaking_hand():
    switch_back()
    return default.action_profile


def stop_sign():
    osascript.run("""tell application "Music"
                        playpause
                    end tell""")
    return action_profile


def drumming_fingers():
    switch_back()
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
