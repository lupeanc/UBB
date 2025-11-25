
#ifndef DATE_H
#define DATE_H
#pragma once
#include <string>
using namespace std;

class Date{
private:
    int day;
    int month;
    int year;

public:
    //empty constructor
    Date();
    // constructor
    Date(int day, int month, int year);

    //getters
    // Gets the day from the struct Date and returns it
    int getDay();
    // Gets the month from the struct Date and returns it
    int getMonth();
    //Gets the year from the struct Date and returns it
    int getYear();

    //setters
    //Sets the day for a struct type Date; param = new value for day
    void setDay(int newDay);
    //Sets the month for a struct type Date; param = new value for month
    void setMonth(int newMonth);
    //Sets the year for a struct type Date; param = new value for year
    void setYear(int newYear);

    //writes a string version of th Date
    string toString();

    //destructor
//    ~Date();
};

#endif //DATE_H
