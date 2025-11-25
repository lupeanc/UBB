
#include "Controller.h"

void Controller::addDepartment(Department* department){
  departments.push_back(department);
}

void Controller::initDepartment(){
  Department* department = new Natal("hos", 10, 12, 14);
  addDepartment(department);
  Department* department2 = new Surgery("hos2", 10, 1);
  addDepartment(department2);
}

vector<Department*> Controller::getDepartments(){
  return departments;
}