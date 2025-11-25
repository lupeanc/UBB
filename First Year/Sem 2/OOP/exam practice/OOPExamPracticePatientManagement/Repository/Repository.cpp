
#include "Repository.h"
#include <fstream>
#include <algorithm>
using namespace std;

void Repository::LoadData(){
  ifstream finDr(R"(F:\c projects uni\OOPExamPracticePatientManagement\Repository\doctors.txt)");
  ifstream finP(R"(F:\c projects uni\OOPExamPracticePatientManagement\Repository\patients.txt)");
  string name, specialization;
  string nameP, diagnosis, specializationP, currentDr, admissionDate;

  doctors.clear();
  while(finDr>>name>>specialization){
    Doctor doctor(name,specialization);
    doctors.push_back(doctor);
  }
  finDr.close();

  patients.clear();
  while(finP>>nameP>>admissionDate>>diagnosis>>specializationP>>currentDr){
    Patient patient(nameP,admissionDate, diagnosis, specializationP,currentDr);
    patients.push_back(patient);
  }
  finP.close();

}

bool compare(Patient a, Patient b){
  return a.getAdmissionDate()<b.getAdmissionDate();
}

vector<Patient> Repository::getPatients(){
  LoadData();
  //maybe move this in load data so that all of the entries are sorted after each modification
  std::sort(patients.begin(), patients.end(), compare);
  return patients;
}

vector<Patient> Repository::getPatientsBySpecialization(string spec) {
  LoadData();
  vector<Patient> pDr;
  for (auto p: patients) {
    if (p.getSpecialization() == spec) {
      cout << p.getName() << endl;
      pDr.push_back(p);
    }
  }

  return pDr;
}

vector<Patient> Repository::getPatientsUndiagnosed() {
  LoadData();
  vector<Patient> pU;
  for (auto p: patients) {
    if (p.getDiagnosis() == "undiagnosed") {
      // cout<<p.getDiagnosis()<<endl;
      pU.push_back(p);
    }
  }
  return pU;
}

void Repository::addPatient(string name, string admissionDate, string diagnosis, string specialization, string currentDr) {
  // vector<Patient> patientsHere = getPatients();
  patients.push_back(Patient(name, admissionDate, diagnosis, specialization, currentDr));

  ofstream foutP(R"(F:\c projects uni\OOPExamPracticePatientManagement\Repository\patients.txt)");

  for (auto p: patients) {
    foutP<<p.toString()<<endl;
  }
  foutP.close();
  LoadData();
  this->notify();

}

void Repository::updatePatient(string name, string what, string update) {
  vector<Patient> patientsNew;

  for (auto p: patients) {
    if (p.getName() == name) {
      if (what == "diagnosis") {
        p.setDiagnosis(update);
      }
      else if (what == "specialization") {
        p.setSpecialization(update);
      }
    }
    patientsNew.push_back(p);
  }

  patients = patientsNew;

  // if (what == "diagnosis") {
  //   for (auto p: patients) {
  //     if (p.getName() == name) {
  //
  //       p.setDiagnosis(update);
  //       patients.push_back(p);
  //       break;
  //     }
  //   }
  // }
  // else if (what == "specialization") {
  //   for (auto p: patients) {
  //     if (p.getName() == name) {
  //
  //       p.setSpecialization(update);
  //       patients.push_back(p);
  //       break;
  //     }
  //
  //   }
  // }

  ofstream foutP(R"(F:\c projects uni\OOPExamPracticePatientManagement\Repository\patients.txt)");

  for (auto p: patientsNew) {
    foutP<<p.toString()<<endl;
  }
  foutP.close();
  LoadData();
  this->notify();

}
