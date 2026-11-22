
#ifndef WEATHER_H
#define WEATHER_H
#include <iostream>
using namespace std;

class Weather{
  private:
    int start;
    int end;
    int pp;
    string description;

    public:
      Weather();
      Weather(int start, int end, int pp, string description);
      ~Weather();
      int getStart();
      int getEnd();
      int getPp();
      string getDescription();
};

#endif //WEATHER_H
