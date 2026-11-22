
#ifndef DISHWASHER_H
#define DISHWASHER_H
#include "Appliance.h"
#pragma once

class Dishwasher: public Appliance{
  private:
    double consumedElecHour;

  public:
    Dishwasher();
    Dishwasher(string id, double consumedElecHour);

    // double consumedElectricity() override;
    string toString() override;

    // double getConsumedElecHour();
//    void setConsumedElecHour(double consumedElecHour);
    ~Dishwasher() override;

};


#endif //DISHWASHER_H
