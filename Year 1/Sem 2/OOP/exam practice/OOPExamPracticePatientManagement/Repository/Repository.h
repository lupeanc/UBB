
#ifndef REPOSITORY_H
#define REPOSITORY_H
#include "../Domain/Doctor.h"
#include "../Domain/Patient.h"
#include <vector>
#include "../Observer.h"


class Repository: public Subject {
  private:
    vector<Doctor> doctors;
    vector<Patient> patients;

    public:
      Repository(){LoadData();};
      void LoadData();
      vector<Doctor> getDoctors(){
        return doctors;
      };
      vector<Patient> getPatients();
      vector<Patient> getPatientsBySpecialization(string specialization);
      vector<Patient> getPatientsUndiagnosed();
      void addPatient(string name, string admissionDate, string diagnosis, string specialization, string currentDr);
      void updatePatient(string name, string what, string update);
      ~Repository()=default;

};



#endif //REPOSITORY_H
