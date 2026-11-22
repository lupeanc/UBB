
#ifndef REFRIGERATOR_H
#define REFRIGERATOR_H
#include "Appliance.h"
#pragma once

class Refrigerator: public Appliance {
  private:
    string usageClass;
    bool hasFreezer;

    public:
      Refrigerator();
      Refrigerator(string id, string usageClass, bool hasFreezer);

      // double consumedElectricity() override;
      string toString() override;

      // string getUsageClass();
      // bool getHasFreezer();
//      void setHasFreezer(bool hasFreezer);
//      void setUsageClass(string usageClass);
      ~Refrigerator() override;
};

#endif //REFRIGERATOR_H
