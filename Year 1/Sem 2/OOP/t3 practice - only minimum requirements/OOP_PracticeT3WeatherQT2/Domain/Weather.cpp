
#include "Weather.h"
Weather::Weather() {

}

Weather::Weather(int start, string desc) {
    this->start = start;
    this->desc = desc;

}


string Weather::toString() {
    string str;
    str = to_string(start) + " " + desc;
    return str;
}

Weather::~Weather(){}
