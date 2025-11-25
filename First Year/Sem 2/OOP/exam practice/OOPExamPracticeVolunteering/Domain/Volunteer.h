
#ifndef VOLUNTEER_H
#define VOLUNTEER_H
#include <iostream>
using namespace std;


class Volunteer {
private:
  string name, email, i1, i2, i3, department;

  public:
    Volunteer();
    Volunteer(string name, string email, string i1, string i2, string i3, string department);
    string getName();
    string getEmail();
    string getI1();
    string getI2();
    string getI3();
    string getDepartment();
    string toString();
    ~Volunteer();
};



#endif //VOLUNTEER_H
