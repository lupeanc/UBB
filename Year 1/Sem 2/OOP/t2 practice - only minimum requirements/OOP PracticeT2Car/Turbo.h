
#ifndef TURBO_H
#define TURBO_H
#include "Engine.h"

class Turbo : public Engine {
  public:
    Turbo();
    Turbo(double price);
    ~Turbo();
    double getPrice();
    string toString() override;
};

#endif //TURBO_H
