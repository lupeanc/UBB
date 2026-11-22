
#ifndef ELECTRIC_H
#define ELECTRIC_H
#include "Engine.h"

class Electric: public Engine {
  private:
    int autonomy;

    public:
      Electric();
      Electric(double price, int autonomy);
      double getPrice();
      string toString() override;
      ~Electric();

};

#endif //ELECTRIC_H
