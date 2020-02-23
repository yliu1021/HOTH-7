//
// Created by Yuhan Liu on 2/23/20.
//

#include <iostream>
#include <filesystem>

#include "HandGesture.h"

using namespace std;

const char *hand_gesture_path = "/Users/yuhanliu/Documents/Hackathons/HOTH/hand.sh";

int main() {
    HandGesture h(hand_gesture_path);
    cout << filesystem::current_path() << endl;
    while (true) {
        ;
    }
}
