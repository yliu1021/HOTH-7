import time

from handmodel import Gesture


from interface.actionprofiles import default


class ComputerInterface:
    def __init__(self):
        self.gesture_hist = list()
        self.active_action_profile = default.action_profile

    def receive_gesture(self, gesture: Gesture):
        self.gesture_hist.append((gesture, time.time()))

        self.active_action_profile = self.active_action_profile[gesture]()
