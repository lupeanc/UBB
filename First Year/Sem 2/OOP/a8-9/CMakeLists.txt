cmake_minimum_required(VERSION 3.30)
project(assignment8_9)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)


find_package(Qt6 COMPONENTS
  Core
  Gui
  Widgets
  REQUIRED)

add_executable(assignment8_9 main.cpp
        AbstractEventsList/AbstractEventsList.h
        AbstractEventsList/AbstractEventsList.cpp
        AdminGUI/AdminGUI.h
        AdminGUI/AdminGUI.cpp
        Console/Console.h
        Console/Console.cpp
        CSVRepository/CSVRepository.h
        CSVRepository/CSVRepository.cpp
        Domain/Date.h
        Domain/Date.cpp
        Domain/Event.h
        Domain/Event.cpp
        Exceptions/Exceptions.h
        Exceptions/Exceptions.cpp
        FileRepository/FileRepository.h
        FileRepository/FileRepository.cpp
        GUI/GUI.h
        GUI/GUI.cpp
        HTMLRepository/HTMLRepository.h
        HTMLRepository/HTMLRepository.cpp
        Repository/Repository.h
        Repository/Repository.cpp
        Validator/Validator.h
        Validator/Validator.cpp
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
        UserGUI/UserGUI.h
        UserGUI/UserGUI.cpp
        DynamicArray.h
)
target_link_libraries(assignment8_9
  Qt::Core
  Qt::Gui
  Qt::Widgets
)

if (WIN32 AND NOT DEFINED CMAKE_TOOLCHAIN_FILE)
    set(DEBUG_SUFFIX)
    if (MSVC AND CMAKE_BUILD_TYPE MATCHES "Debug")
        set(DEBUG_SUFFIX "d")
    endif()
    set(QT_INSTALL_PATH "${CMAKE_PREFIX_PATH}")
    if(NOT EXISTS "${QT_INSTALL_PATH}/bin")
        set(QT_INSTALL_PATH "${QT_INSTALL_PATH}/..")
        if(NOT EXISTS "${QT_INSTALL_PATH}/bin")
            set(QT_INSTALL_PATH "${QT_INSTALL_PATH}/..")
        endif()
    endif()
    if(EXISTS "${QT_INSTALL_PATH}/plugins/platforms/qwindows${DEBUG_SUFFIX}.dll")
        add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E make_directory
                "$<TARGET_FILE_DIR:${PROJECT_NAME}>/plugins/platforms/")
        add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy
                "${QT_INSTALL_PATH}/plugins/platforms/qwindows${DEBUG_SUFFIX}.dll"
                "$<TARGET_FILE_DIR:${PROJECT_NAME}>/plugins/platforms/")
    endif()
    foreach(QT_LIB Core Gui Widgets )
        add_custom_command(TARGET ${PROJECT_NAME} POST_BUILD
                COMMAND ${CMAKE_COMMAND} -E copy
                "${QT_INSTALL_PATH}/bin/Qt6${QT_LIB}${DEBUG_SUFFIX}.dll"
                "$<TARGET_FILE_DIR:${PROJECT_NAME}>")
    endforeach(QT_LIB)
endif()
