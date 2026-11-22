
#include "Repository.h"
#include <fstream>
#include <cmath>
void Repository::LoadData(){
  ifstream finD(R"(F:\c projects uni\OOPExamPracticeDriveConnect\drivers)");
  string name;
  int xloc, yloc, score;

  drivers.clear();
  while(finD>>name>>xloc>>yloc>>score){
    drivers.push_back(Driver(name,xloc,yloc,score));
  }
  finD.close();

  ifstream finR(R"(F:\c projects uni\OOPExamPracticeDriveConnect\reports)");

  string desc, status;

  reports.clear();
  while(finR>>desc>>name>>xloc>>yloc>>status){
    if(status == "true")
    reports.push_back(Report(desc,name,xloc,yloc,true));
    else
      reports.push_back(Report(desc,name,xloc,yloc,false));
  }
  finR.close();

}

vector<Driver> Repository::getDrivers(){
  LoadData();
  return drivers;
}

vector<Report> Repository::getReports(){
  LoadData();
  return reports;
}

vector<Report> Repository::getReportsRegion(Driver d){
  LoadData();
  vector<Report> regionReports;

  for(auto r: reports){
    int formula = sqrt(pow((d.getXloc()-r.getXloc()), 2)+pow((d.getYloc()-r.getYloc()), 2));
    if(formula < 10)
      regionReports.push_back(r);
  }

  return regionReports;
}

void Repository::writeToFile(){
  ofstream fout(R"(F:\c projects uni\OOPExamPracticeDriveConnect\reports)");

  for(auto report : reports){
    fout<<report.toString()<<endl;
  }
  fout.close();
  this->notify();
}

void Repository::addReport(Report r){
  reports.push_back(r);
  writeToFile();
}