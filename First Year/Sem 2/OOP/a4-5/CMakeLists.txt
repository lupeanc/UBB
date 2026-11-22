cmake_minimum_required(VERSION 3.30)
project(assignment_4_5)

set(CMAKE_CXX_STANDARD 20)

add_executable(assignment_4_5
        main.cpp
        Console/Console.h
        Console/Console.cpp
        Domain/Date.h
        Domain/Date.cpp
        Domain/Event.h
        Domain/Event.cpp
        Repository/Repository.h
        Repository/Repository.cpp
        Service/Service.h
        Service/Service.cpp
        Tests/test_domain.h
        Tests/test_domain.cpp
        Tests/test_dyn_arr.h
        Tests/test_dyn_arr.cpp
        Tests/test_domain.cpp
        Tests/test_repo.h
        Tests/test_repo.cpp
        Tests/test_service.h
        Tests/test_service.cpp
        Tests/test_validation.h
        Tests/test_validation.cpp
        Validator/Validator.h
        Validator/Validator.cpp
        DynamicArray.h
)
