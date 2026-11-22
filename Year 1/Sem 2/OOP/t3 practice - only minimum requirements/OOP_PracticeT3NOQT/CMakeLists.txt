cmake_minimum_required(VERSION 3.30)
project(OOP_PracticeT3Weather)

set(CMAKE_CXX_STANDARD 20)

add_executable(OOP_PracticeT3Weather
        main.cpp
        Domain/Weather.h
        Domain/Weather.cpp
        Repository/Repository.h
        Repository/Repository.cpp
)
