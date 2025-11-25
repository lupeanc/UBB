
#ifndef HOUSE_H
#define HOUSE_H
#include "Building.h"

class House: public Building{
  private:
    string type;
    bool historical;

    public:
      House();
      House(string address, int constrYear, string type, bool historical);
      string toString() override;
      ~House();
};

#endif //HOUSE_H
