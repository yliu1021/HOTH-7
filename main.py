import sys

from handmodel import InferenceModel
from interface import ComputerInterface


def main(debug=False):
    interface = ComputerInterface()

    inference_model = InferenceModel(threshold=0.75, gesture_duration_threshold=0.5, repeat_threshold=5)
    inference_model.start_inference()
    gesture_queue = inference_model.gesture_queue
    try:
        while True:
            gesture, confidence = gesture_queue.get(block=True)
            print(gesture, confidence, flush=True)
            # interface.receive_gesture(gesture)
            if debug:
                print('{:.3f}: {}'.format(confidence, gesture))
    except KeyboardInterrupt:
        print('\rCleaning up...', flush=True, end=' ')
        inference_model.stop_inference()
        print('Done')
        exit(0)


if __name__ == '__main__':
    main(debug=('debug' in sys.argv))
