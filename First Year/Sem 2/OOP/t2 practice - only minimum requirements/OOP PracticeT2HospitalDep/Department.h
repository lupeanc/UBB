
#ifndef DEPARTMENT_H
#define DEPARTMENT_H
#include <iostream>
using namespace std;

class Department {
  protected:
    string name;
    int nbDr;
    public:
      string getName();
      int getNbDr();
      void setName(string name);
      void setNbDr(int nbDr);
      virtual string toString()=0;

};

#endif //DEPARTMENT_H
