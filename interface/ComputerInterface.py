import time

from handmodel import Gesture


from interface.actionprofiles import default


class ComputerInterface:
    def __init__(self):
        self.gesture_hist = list()
        self.active_action_profile = default.action_profile

    def receive_gesture(self, gesture: Gesture):
        if gesture == Gesture.SlidingTwoFingersDown and len(self.gesture_hist) > 0:
            last_gesture, last_gesture_time = self.gesture_hist[-1]
            now = time.time()
            if now - last_gesture_time <= 1.0:
                return
        self.gesture_hist.append((gesture, time.time()))
        self.active_action_profile = self.active_action_profile[gesture]()
