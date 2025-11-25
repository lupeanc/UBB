
#ifndef BUILDING_H
#define BUILDING_H
#include <iostream>
using namespace std;

class Building {
  protected:
    string address;
    int constrYear;

    public:
    // Building();
    // Building(string address, int constrYear);
    // virtual ~Building() = default;

    virtual string toString() = 0;


};

#endif //BUILDING_H
