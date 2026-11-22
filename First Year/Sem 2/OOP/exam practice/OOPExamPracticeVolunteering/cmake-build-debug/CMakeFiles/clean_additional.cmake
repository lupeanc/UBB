# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\OOPExamPracticeVolunteering_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\OOPExamPracticeVolunteering_autogen.dir\\ParseCache.txt"
  "OOPExamPracticeVolunteering_autogen"
  )
endif()
