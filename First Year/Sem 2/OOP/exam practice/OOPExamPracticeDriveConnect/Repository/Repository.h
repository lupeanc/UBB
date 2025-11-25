
#ifndef REPOSITORY_H
#define REPOSITORY_H
#include "../Domain/Driver.h"
#include "../Domain/Report.h"
#include <iostream>
#include <vector>
#include "../Observer.h"
using namespace std;

class Repository: public Subject {
  private:
    vector<Driver> drivers;
    vector<Report> reports;

    public:
      Repository(){LoadData();}
      vector<Driver> getDrivers();
      vector<Report> getReports();
      vector<Report> getReportsRegion(Driver d);
      void LoadData();
      void writeToFile();
      void addReport(Report r);
      ~Repository()=default;


};



#endif //REPOSITORY_H
