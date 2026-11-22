
#ifndef ENGINE_H
#define ENGINE_H
#include <iostream>
using namespace std;

class Engine{
  protected:
    double price;
    public:
      int getPrice();
      virtual string toString()=0;
};

#endif //ENGINE_H
