# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles\\OOPExamPracticeQuiz2_autogen.dir\\AutogenUsed.txt"
  "CMakeFiles\\OOPExamPracticeQuiz2_autogen.dir\\ParseCache.txt"
  "OOPExamPracticeQuiz2_autogen"
  )
endif()
