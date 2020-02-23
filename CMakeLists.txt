cmake_minimum_required(VERSION 2.8.9)
project (main)

set (CMAKE_CXX_STANDARD 17)

include_directories(include)
file(GLOB SOURCES "src/*.cpp" "main.cpp")

add_executable(main ${SOURCES})
