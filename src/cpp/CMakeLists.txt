cmake_minimum_required(VERSION 3.27)
project(cpp)

set(CMAKE_CXX_STANDARD 14)

include_directories(sw/sa_pipeline)

add_executable(cpp
        sw/sa_pipeline/sa_defs.h
        sw/sa_pipeline/sa_pipeline_sw.cpp
        sw/sa_pipeline/stage0_sa.cpp
        sw/sa_pipeline/stage1_sa.cpp
        sw/sa_pipeline/stage2_sa.cpp
        sw/sa_pipeline/stage3_sa.cpp
        sw/sa_pipeline/stage4_sa.cpp
        sw/sa_pipeline/stage5_sa.cpp
        sw/sa_pipeline/stage6_sa.cpp
        sw/sa_pipeline/stage7_sa.cpp
        sw/sa_pipeline/stage8_sa.cpp
        sw/sa_pipeline/stage9_sa.cpp
        util/pipeline_base.cpp)
