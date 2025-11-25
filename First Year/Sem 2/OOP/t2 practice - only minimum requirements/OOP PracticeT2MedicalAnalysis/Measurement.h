
#ifndef MEASUREMENT_H
#define MEASUREMENT_H
#include <iostream>
using namespace std;

class Measurement{
  protected:
    string date;

  public:
    virtual string toString() = 0;
    // ~Measurement(){}
};
#endif //MEASUREMENT_H
