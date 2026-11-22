
#include "Repository.h"
#include <fstream>
#include <algorithm>

Repository::Repository(){
  LoadData();
}

bool compare(Volunteer a, Volunteer b){
  return a.getName() < b.getName();
}

void Repository::LoadData(){
  ifstream finDep(R"(F:\\c projects uni\\OOPExamPracticeVolunteering\\departments.txt)");
  ifstream finVol(R"(F:\c projects uni\OOPExamPracticeVolunteering\volunteers.txt)");

  string nameDepartment, desc1, desc2, desc3, desc4, desc5;
  string nameVolunteer, email, i1, i2, i3, department;

  this->departments.clear();
  while(finDep>>nameDepartment>>desc1>>desc2>>desc3>>desc4>>desc5){
    Department d = Department(nameDepartment, desc1, desc2, desc3, desc4, desc5);
    departments.push_back(d);
  }
  finDep.close();

  volunteers.clear();
  while(finVol>>nameVolunteer>>email>>i1>>i2>>i3>>department){
    Volunteer v(nameVolunteer, email, i1, i2, i3, department);
    volunteers.push_back(v);
  }
  finVol.close();
  std::sort(volunteers.begin(), volunteers.end(), compare);
}

vector<Department> Repository::getDepartments(){
  LoadData();
  return departments;
}

vector<Volunteer> Repository::getVolunteers(){
  LoadData();
  return volunteers;
}

vector<Volunteer> Repository::getVolunteersDep(string department){
  LoadData();
  vector<Volunteer> v = this->getVolunteers();
  vector<Volunteer> depV;
  depV.clear();

  for(auto volunteer : v){
    if(volunteer.getDepartment() == department){
      depV.push_back(volunteer);
    }
  }
  return depV;
}

vector<Volunteer> Repository::getVolunteersNonDep(){
  LoadData();
  vector<Volunteer> v = this->getVolunteers();
  vector<Volunteer> depNV;
  depNV.clear();

  for(auto volunteer : v){
    if(volunteer.getDepartment() == "none"){
      depNV.push_back(volunteer);
    }
  }
  return depNV;
}


// vector<Department> Repository::getDepartmentsSorted() {
//   LoadData();
//
//   for (auto d: departments) {
//     int n = this->getVolunteersDep(d.getName()).size();
//     v.push_back(d);
//   }
//
// }

void Repository::addVolunteer(string name, string email, string i1, string i2, string i3, string dep) {
  Volunteer v(name, email, i1, i2, i3, dep);
  volunteers.push_back(v);

  ofstream fout(R"(F:\c projects uni\OOPExamPracticeVolunteering\volunteers.txt)");

  for (auto volunteer : volunteers) {
    fout<<volunteer.toString()<<endl;
  }
  fout.close();
  LoadData();
  this->notify();
}

bool compareNr(DepNrVol d1, DepNrVol d2) {
  return d1.n<d2.n;
}

vector<DepNrVol> Repository::getDepNrVol() {
  LoadData();
  for (auto d: departments) {
    DepNrVol dNr(d, getNumberVolunteers(d));
    depNrVol.push_back(dNr);
  }
  std::sort(depNrVol.begin(), depNrVol.end(), compareNr);
  return depNrVol;
}

int Repository::getNumberVolunteers(Department d) {
  return getVolunteersDep(d.getName()).size();
}

