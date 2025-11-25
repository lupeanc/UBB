
#ifndef PERSON_H
#define PERSON_H
#include <iostream>
using namespace std;


class Person {
  string name;
  int xloc, yloc;
  bool status;

  public:
    Person(){}
    Person(string name, int xloc, int yloc, bool status) {
      this->name = name;
      this->xloc = xloc;
      this->yloc = yloc;
      this->status = status;
    }
    string getName() {
      return this->name;
    }
    bool getStatus() {
      return this->status;
    }
    int getXloc() {
      return this->xloc;
    }
    int getYloc() {
      return this->yloc;
    }
    string toString();
    ~Person(){}

};



#endif //PERSON_H
