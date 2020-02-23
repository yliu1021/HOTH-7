import sys
import os
import time
from enum import Enum
from collections import deque
from queue import Queue
from threading import Thread

import numpy as np
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras.models import load_model
import cv2


class Gesture(Enum):
    SwipingLeft = 'swipe left'
    SwipingRight = 'swipe right'
    SwipingDown = 'swipe down'
    SwipingUp = 'swipe up'
    PushingHandAway = 'pushing hand away'
    PullingHandIn = 'pulling hand in'
    SlidingTwoFingersLeft = 'sliding two fingers left'
    SlidingTwoFingersRight = 'sliding two fingers right'
    SlidingTwoFingersDown = 'sliding two fingers down'
    SlidingTwoFingersUp = 'sliding two fingers up'
    PushingTwoFingersAway = 'pushing two fingers away'
    PullingTwoFingersIn = 'pulling two fingers in'
    RollingHandForward = 'rolling hand forward'
    RollingHandBackward = 'rolling hand backward'
    TurningHandClockwise = 'turning hand clockwise'
    TurningHandCounterclockwise = 'turning hand counterclockwise'
    ZoomingInWithFullHand = 'zooming in with full hand'
    ZoomingOutWithFullHand = 'zooming out with full hand'
    ZoomingInWithTwoFingers = 'zooming in with two fingers'
    ZoomingOutWithTwoFingers = 'zooming out with two fingers'
    ThumbUp = 'thumb up'
    ThumbDown = 'thumb down'
    ShakingHand = 'shaking hand'
    StopSign = 'stop sign'
    DrummingFingers = 'drumming fingers'
    NoGesture = 'no gesture'
    DoingOtherThings = 'doing other things'


GESTURES = [
    Gesture.SwipingLeft,
    Gesture.SwipingRight,
    Gesture.SwipingDown,
    Gesture.SwipingUp,
    Gesture.PushingHandAway,
    Gesture.PullingHandIn,
    Gesture.SlidingTwoFingersLeft,
    Gesture.SlidingTwoFingersRight,
    Gesture.SlidingTwoFingersDown,
    Gesture.SlidingTwoFingersUp,
    Gesture.PushingTwoFingersAway,
    Gesture.PullingTwoFingersIn,
    Gesture.RollingHandForward,
    Gesture.RollingHandBackward,
    Gesture.TurningHandClockwise,
    Gesture.TurningHandCounterclockwise,
    Gesture.ZoomingInWithFullHand,
    Gesture.ZoomingOutWithFullHand,
    Gesture.ZoomingInWithTwoFingers,
    Gesture.ZoomingOutWithTwoFingers,
    Gesture.ThumbUp,
    Gesture.ThumbDown,
    Gesture.ShakingHand,
    Gesture.StopSign,
    Gesture.DrummingFingers,
    Gesture.NoGesture,
    Gesture.DoingOtherThings
]


class InferenceModel:
    def __init__(self, single_frame_model_loc='models/single_frame.h5', multi_frame_model_loc='models/multi_frame.h5',
                 threshold=0.95, gesture_duration_threshold=1.0, repeat_threshold=3):
        self.single_frame_model = load_model(single_frame_model_loc)
        self.multi_frame_model = load_model(multi_frame_model_loc)

        self.encoded_frames = deque()
        for i in range(12):
            self.encoded_frames.append(np.zeros(shape=(4, 6, 1280), dtype=np.float32))

        self.gesture_queue = Queue()
        self._unfiltered_gesture_queue = Queue()

        self.threshold = threshold
        self.gesture_duration_threshold = gesture_duration_threshold
        self.repeat_threshold = repeat_threshold

        self.looping = False
        self.inference_thread = Thread(target=self.stream_inferences)
        self._inference_thread = Thread(target=self.inference_loop)

    def start_inference(self):
        self.looping = True
        self.gesture_queue = Queue()
        self._unfiltered_gesture_queue = Queue()
        self.inference_thread.start()

    def stop_inference(self):
        self.looping = False
        self.inference_thread.join()
        self._inference_thread.join()

    def stream_inferences(self):
        self._inference_thread.start()

        previous_gestures = dict()
        for gesture in GESTURES:
            previous_gestures[gesture] = [(gesture, 0.)]

        while self.looping:
            gesture_pred = self._unfiltered_gesture_queue.get(block=True)
            if gesture_pred.max() < self.threshold:
                continue
            gesture_time = time.time()
            gesture = GESTURES[gesture_pred.argmax()]
            prev_same_gestures = previous_gestures[gesture]
            if gesture_time - prev_same_gestures[-1][1] > self.gesture_duration_threshold:
                previous_gestures[gesture] = [(gesture, gesture_time)]
            else:
                previous_gestures[gesture].append((gesture, gesture_time))

            if len(previous_gestures[gesture]) == self.repeat_threshold:
                confidence = gesture_pred.max()
                self.gesture_queue.put((gesture, confidence))

    def inference_loop(self):
        cap = cv2.VideoCapture(0)
        times = list()
        while self.looping:
            start = time.time()

            ret, frame = cap.read()
            frame = cv2.resize(frame, (192, 108))
            frame = frame.astype(np.float32) / 127.5 - 1

            encoded_frame = self.single_frame_model.predict(frame[None, ...])
            encoded_frame = np.reshape(encoded_frame, (4, 6, 1280))

            self.encoded_frames.append(encoded_frame)
            self.encoded_frames.popleft()

            encoded_frame_np = np.array(self.encoded_frames)
            pred = self.multi_frame_model.predict(encoded_frame_np[None, ...])[0, 0]
            pred = np.exp(pred - np.max(pred))
            pred /= pred.sum()
            self._unfiltered_gesture_queue.put(pred)

            end = time.time()
            wait_time = max(1, int((1/10 - (end - start)) * 1000))
            cv2.waitKey(wait_time)
