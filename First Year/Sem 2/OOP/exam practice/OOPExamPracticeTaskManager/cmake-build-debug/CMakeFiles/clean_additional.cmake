# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\OOPExamPracticeTaskManager_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\OOPExamPracticeTaskManager_autogen.dir\\ParseCache.txt"
  "OOPExamPracticeTaskManager_autogen"
  )
endif()
