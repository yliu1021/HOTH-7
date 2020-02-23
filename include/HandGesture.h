//
// Created by Yuhan Liu on 2/23/20.
//

#ifndef MAIN_HANDGESTURE_H
#define MAIN_HANDGESTURE_H

// Set this to the directory containing the main.py Python file
const char *hand_gesture_path = "/Users/yuhanliu/Documents/Hackathons/HOTH";

class HandGesture {
public:
    explicit HandGesture(const char *rd);
private:
    const char *root_dir;
};


#endif //MAIN_HANDGESTURE_H
