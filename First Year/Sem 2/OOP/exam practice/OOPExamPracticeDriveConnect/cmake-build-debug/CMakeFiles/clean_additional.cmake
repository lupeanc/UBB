# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\OOPExamPracticeDriveConnect_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\OOPExamPracticeDriveConnect_autogen.dir\\ParseCache.txt"
  "OOPExamPracticeDriveConnect_autogen"
  )
endif()
