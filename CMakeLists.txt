cmake_minimum_required(VERSION 3.29)
project(PeR)

set(CMAKE_CXX_STANDARD 14)

include_directories(src/cpp/src)

add_executable(PeR
    src/cpp/src/graph.cpp
    src/cpp/src/graph.h)
