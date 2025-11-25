
#ifndef DEPNRVOL_H
#define DEPNRVOL_H
#include "Department.h"
#include "../Repository/Repository.h"


class DepNrVol {
public:
      Department department;
      int n;


        DepNrVol(Department d, int n){
          this->department = d;
          this->n = n;
          }
        string toString() {
            return department.getName() + " " + to_string(n);
        }
};



#endif //DEPNRVOL_H
