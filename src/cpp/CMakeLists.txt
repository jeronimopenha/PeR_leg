cmake_minimum_required(VERSION 3.27)
project(cpp)

set(CMAKE_CXX_STANDARD 14)

include_directories(sw/sa_pipeline)

add_executable(cpp
        sw/sa_pipeline/main.cpp
        sw/sa_pipeline/sa_pipeline_sw.h
        sw/sa_pipeline/sa_pipeline_sw.cpp
        sw/sa_pipeline/stage0_sa.h
        sw/sa_pipeline/stage0_sa.cpp
        sw/sa_pipeline/stage1_sa.h
        sw/sa_pipeline/stage1_sa.cpp
        sw/sa_pipeline/stage1_sa.cpp
        sw/sa_pipeline/fifo_sa.cpp
        sw/sa_pipeline/fifo_sa.h)
