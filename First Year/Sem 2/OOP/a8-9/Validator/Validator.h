
#ifndef VALIDATOR_H
#define VALIDATOR_H
#pragma once
#include "../Domain/Event.h"
#include <string>
using namespace std;
class Validator {
    public:
        //checks if the elements for the Date struct are valid
        // all > 0
        // day<31 ; month < 13, year can only be 2024 and 2025
          bool validateDate(int day, int month, int year);
        //validates the time
        // 0<= time <= 24
          bool validateTime(int time);
        //validates attendance
        //attendance > 0
          bool validateAttendance(int attendance);
};
#endif //VALIDATOR_H
