//
// Created by Yuhan Liu on 2/23/20.
//

#include "HandGesture.h"

#ifdef _WIN32

#include <iostream>

HandGesture::HandGesture(const char *rd) : root_dir(rd) {
    // blah blah blah
    std::cout << "hi" << std::endl;
}

#else

#include <unistd.h>
#include <cstdio>
#include <string>

using namespace std;

HandGesture::HandGesture(const char *rd) {
    string root_dir(rd);
    string hand_file = root_dir + "hand.sh";

    int pipe_fd[2];

    if (pipe(pipe_fd) == -1) {
        perror("pipe error");
        return;
    }
    out_fd = pipe_fd[0];

    pid_t cpid = fork();
    if (cpid == -1) {
        perror("fork error\n");
        return;
    }
    if (cpid == 0) {
        close(STDOUT_FILENO);
        dup(pipe_fd[1]);
        close(pipe_fd[1]);
        execlp("bash", "bash", hand_file.c_str(), root_dir.c_str(), hand_file.c_str(), NULL);
    }
}

#endif
