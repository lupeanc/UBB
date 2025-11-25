
#ifndef WEATHER_H
#define WEATHER_H
#include <iostream>
using namespace std;


class Weather {
private:
    int start;
    string desc;

    public:
    Weather();
    Weather(int start, string desc);
    ~Weather();

    string toString();

};



#endif //WEATHER_H
