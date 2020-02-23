//
// Created by Yuhan Liu on 2/23/20.
//

#include <iostream>
#include <unistd.h>

#include "HandGesture.h"

using namespace std;

const char *hand_gesture_path = "/Users/yuhanliu/Documents/Hackathons/HOTH/";

int main() {
    HandGesture h(hand_gesture_path);
    char buffer[128];
    buffer[127] = '\0';
    for (int i = 0; i < 10; ++i) {
        ssize_t bytes_read = read(h.get_out_fd(), buffer, 2);
        cout << buffer;
    }
}
