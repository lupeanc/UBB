# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\assignment8_9_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\assignment8_9_autogen.dir\\ParseCache.txt"
  "assignment8_9_autogen"
  )
endif()
