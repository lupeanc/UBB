
#ifndef REPOSITORY_H
#define REPOSITORY_H
#include "../Domain/Department.h"
#include "../Domain/Volunteer.h"
#include <vector>
#include "../Observer.h"
#include "../Domain/DepNrVol.h"


class Repository: public Subject {
  private:
    vector<Department> departments;
    vector<Volunteer> volunteers;
    vector<DepNrVol> depNrVol;

    public:
      Repository();
      void LoadData();
      vector<Department> getDepartments();
      vector<Volunteer> getVolunteers();
      vector<Volunteer> getVolunteersDep(string department);
      vector<Volunteer> getVolunteersNonDep();
      vector<DepNrVol> getDepNrVol();
        int getNumberVolunteers(Department d);
      // vector<Department> getDepartmentsSorted();
      void addVolunteer(string name, string email, string i1, string i2, string i3, string dep);
      ~Repository()=default;


};



#endif //REPOSITORY_H
