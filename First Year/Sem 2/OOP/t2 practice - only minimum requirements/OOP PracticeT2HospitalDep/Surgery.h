
#ifndef SURGERY_H
#define SURGERY_H
#include "Department.h"

class Surgery : public Department{
  private:
    int nbPatients;

    public:
      Surgery();
      Surgery(string name, int nbDr, int nbPatients);
      string toString() override;
      ~Surgery();
};

#endif //SURGERY_H
