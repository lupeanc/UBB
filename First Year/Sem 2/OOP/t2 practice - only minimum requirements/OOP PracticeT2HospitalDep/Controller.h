
#ifndef CONTROLLER_H
#define CONTROLLER_H
#include "Department.h"
#include "Natal.h"
#include "Surgery.h"
#include <vector>
class Controller{
  private:
    vector<Department*> departments;

    public:
      void addDepartment(Department* department);
      void initDepartment();
      vector<Department*> getDepartments();
};

#endif //CONTROLLER_H
