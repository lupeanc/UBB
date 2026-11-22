
#ifndef DOCTOR_H
#define DOCTOR_H
#include <string>
using namespace std;


class Doctor {
  string name, specialization;
  public:
    Doctor();
    Doctor(string name, string specialization);
    string getName();
    string getSpecialization();
    ~Doctor()=default;

};



#endif //DOCTOR_H
