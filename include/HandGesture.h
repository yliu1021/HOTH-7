//
// Created by Yuhan Liu on 2/23/20.
//

#ifndef MAIN_HANDGESTURE_H
#define MAIN_HANDGESTURE_H

#ifndef _WIN32
#include <unistd.h>
#endif

class HandGesture {
public:
    explicit HandGesture(const char *rd);
    int get_out_fd() const { return out_fd; }
private:
    int out_fd;
};

#endif //MAIN_HANDGESTURE_H
