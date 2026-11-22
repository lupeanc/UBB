#include <string>
#include "test_validation.h"
#include "../Validator/validator.h"
#include <assert.h>
using namespace std;

void testValidation::testValidateDate(){
  Validator* validator = new Validator();
  assert(validator->validateDate(1, 2, 2025));
  assert(!validator->validateDate(0, 2, 2025));
  assert(!validator->validateDate(1, 14, 2025));
  assert(!validator->validateDate(1, 2, 2));
  delete validator;
}

void testValidation::testValidateTime(){
  Validator* validator = new Validator();
  assert(validator->validateTime(1));
  assert(!validator->validateTime(25));
}

void testValidation::testValidateAttendance(){
  Validator* validator = new Validator();
  assert(validator->validateAttendance(1));
  assert(!validator->validateAttendance(-1));
}

void testValidation::testAllValidation(){
  testValidateDate();
  testValidateTime();
  testValidateAttendance();
}