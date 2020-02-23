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
#include <fcntl.h>
#include <cstdio>

HandGesture::HandGesture(const char *rd) : root_dir(rd) {
    int pipe_fd[2];

    pid_t cpid;

    if (pipe(pipe_fd) == -1) {
        perror("pipe error");
        return;
    }

    cpid = fork();
    if (cpid == -1) {
        perror("fork error");
        return;
    }
    if (cpid == 0) {    /* Child reads from pipe */
        close(STDOUT_FILENO);
        dup(pipe_fd[1]);
        execlp("bash", "bash", rd, NULL);
    } else {            /* Parent writes argv[1] to pipe */

    }
}

#endif
