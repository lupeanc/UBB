# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\OOP_PracticeT3Character_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\OOP_PracticeT3Character_autogen.dir\\ParseCache.txt"
  "OOP_PracticeT3Character_autogen"
  )
endif()
