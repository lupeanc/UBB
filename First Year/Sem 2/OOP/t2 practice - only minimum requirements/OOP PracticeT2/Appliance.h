
#ifndef APPLIANCE_H
#define APPLIANCE_H
#pragma once
#include <vector>
#include <iostream>
using namespace std;

class Appliance{
  protected:
    string id;

  public:
//    Appliance();
//    Appliance(string id);
    // virtual double consumedElectricity() = 0;
    virtual string toString() = 0;

  // string getId();
  // void setId(string id);

    virtual ~Appliance();

};

#endif //APPLIANCE_H
