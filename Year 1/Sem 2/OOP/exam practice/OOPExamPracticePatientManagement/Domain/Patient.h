
#ifndef PATIENT_H
#define PATIENT_H
#include<iostream>
using namespace std;


class Patient {
    private:
      string name, diagnosis, specialization, currentDr, admissionDate;
      public:
        Patient(){};
        Patient(string name, string admissionDate, string diagnosis, string specialization, string currentDr){
          this->name = name;
          this->admissionDate = admissionDate;
          this->diagnosis = diagnosis;
          this->specialization = specialization;
          this->currentDr = currentDr;

        };

        string getName(){
          return name;
        };
        string getDiagnosis(){
          return diagnosis;
        };
        string getSpecialization(){
          return specialization;
        };
        string getCurrentDr(){
          return currentDr;
        };
        string getAdmissionDate(){
          return admissionDate;
        };

        void setDiagnosis(string diag) {
          this->diagnosis = diag;
        }

        void setSpecialization(string spec) {
          this->specialization = spec;
        }

        string toString();

        ~Patient()=default;

};



#endif //PATIENT_H
