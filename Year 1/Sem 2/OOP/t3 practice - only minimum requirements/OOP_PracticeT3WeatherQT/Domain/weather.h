
#ifndef WEATHER_H
#define WEATHER_H
#include <iostream>
using namespace std;

class weather {
private:
  int start;
  int end;
  int pp;
  string description;

  public:
    weather();
    weather(int start, int end, int pp, string description);
    ~weather();

    int getStart();
    int getEnd();
    int getPp();
    string getDescription();

    string toString();
};



#endif //WEATHER_H
