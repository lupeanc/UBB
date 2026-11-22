
#ifndef DEPARTMENT_H
#define DEPARTMENT_H
#include <iostream>
using namespace std;



class Department {
  private:
    string name;
    string desc1, desc2, desc3, desc4, desc5;

    public:
      Department();
      Department(string name, string desc1, string desc2, string desc3, string desc4, string desc5);
      string getName();
      string getDesc1();
      string getDesc2();
      string getDesc3();
      string getDesc4();
      string getDesc5();
    string getDescription();
      // string toString();
      ~Department()=default;

};



#endif //DEPARTMENT_H
