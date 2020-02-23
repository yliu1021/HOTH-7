import time
import pyautogui

from handmodel import Gesture


class ComputerInterface:
    def __init__(self):
        ...

    def receive_gesture(self, gesture: Gesture):
        if gesture == Gesture.SwipingLeft:
            pyautogui.hotkey('ctrl', 'right')
        elif gesture == Gesture.SwipingRight:
            pyautogui.hotkey('ctrl', 'left')
        elif gesture == Gesture.SwipingUp:
            pyautogui.hotkey('ctrl', 'up')
        elif gesture == Gesture.SwipingDown:
            pyautogui.hotkey('ctrl', 'down')
        elif gesture == Gesture.SlidingTwoFingersUp:
            for i in range(10):
                pyautogui.scroll(-1)
        elif gesture == Gesture.SlidingTwoFingersDown:
            for i in range(10):
                pyautogui.scroll(1)
        elif gesture == Gesture.SlidingTwoFingersRight:
            for i in range(10):
                pyautogui.hscroll(-1)
        elif gesture == Gesture.SlidingTwoFingersLeft:
            for i in range(10):
                pyautogui.hscroll(1)
        elif gesture == Gesture.ZoomingInWithFullHand:
            pyautogui.hotkey('command', '+')
        elif gesture == Gesture.ZoomingOutWithFullHand:
            pyautogui.hotkey('command', '-')
        elif gesture == Gesture.PushingHandAway:
            pyautogui.hotkey('f11')
        elif gesture == Gesture.PullingHandIn:
            pyautogui.hotkey('f12')
