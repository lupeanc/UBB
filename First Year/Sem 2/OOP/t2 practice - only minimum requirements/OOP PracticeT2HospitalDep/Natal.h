
#ifndef NATAL_H
#define NATAL_H
#include "Department.h"

class Natal:public Department{
  private:
    int nbMothers;
    int nbNewborns;

    public:
      Natal();
      Natal(string name, int nbDr, int nbMothers, int nbNewborns);
      ~Natal();
      string toString() override;
};

#endif //NATAL_H
