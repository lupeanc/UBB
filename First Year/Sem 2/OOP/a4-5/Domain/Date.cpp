#include "Date.h"

Date::Date(){}
Date::Date(int newDay, int newMonth, int newYear){
  this->day = newDay;
  this->month = newMonth;
  this->year = newYear;
}

int Date::getDay(){
  return this->day;
}
int Date::getMonth(){
  return this->month;
}
int Date::getYear(){
  return this->year;
}

void Date::setDay(int newDay){
  this->day = newDay;
}
void Date::setMonth(int newMonth){
  this->month = newMonth;
}
void Date::setYear(int newYear){
  this->year = newYear;
}

string Date::toString() {
  string dateString;
  dateString += std::to_string(this->day);
  dateString += ".";
  dateString += std::to_string(this->month);
  dateString += ".";
  dateString += std::to_string(this->year);
  return dateString;
}
