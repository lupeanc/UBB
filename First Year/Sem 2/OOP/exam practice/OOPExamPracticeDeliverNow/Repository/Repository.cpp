
#include "Repository.h"
#include <fstream>
#include<algorithm>

void Repository::LoadData(){
  ifstream finC(R"(F:\c projects uni\OOPExamPracticeDeliverNow\couriers.txt)");
  ifstream finP(R"(F:\c projects uni\OOPExamPracticeDeliverNow\packages.txt)");

  string name, st1, st2, st3;
  int xcenter, ycenter, r;

  string recipient, st, status;
  int nr, xloc, yloc;

  couriers.clear();
  while(finC>>name>>st1>>st2>>st3>>xcenter>>ycenter>>r){
    Zone z(xcenter,ycenter,r);
    couriers.push_back(Courier(name,st1,st2,st3,z));
  }
  finC.close();

  packages.clear();
  while(finP>>recipient>>st>>nr>>xloc>>yloc>>status){
    bool s;
    if(status == "1")
      s = true;
    else
      s = false;

    packages.push_back(Package(recipient,st,nr,xloc, yloc, s));
  }
  finP.close();

}

vector<Courier> Repository::getCouriers(){
  return couriers;
}

vector<Package> Repository::getPackages(){
  LoadData();
  return packages;
}

vector<Package> Repository::getUndeliveredAssigned(Courier courier){
  LoadData();
  vector<Package> undelivered;
  string st1 = courier.getSt1();
  string st2 = courier.getSt2();
  string st3 = courier.getSt3();

  for(auto p: packages){
    if(p.getStatus() == "0"){
      if(p.getStr() == st1 || p.getStr() == st2 || p.getStr() == st3){
        undelivered.push_back(p);
      }
    }
  }

  return undelivered;

}

void Repository::writeToFile() {
  ofstream fout(R"(F:\c projects uni\OOPExamPracticeDeliverNow\packages.txt)");

  for (auto p: packages) {
    fout<<p.toString()<<endl;
  }
}

void Repository::addPackage(Package package) {
  // LoadData();
  packages.push_back(package);

  ofstream fout(R"(F:\c projects uni\OOPExamPracticeDeliverNow\packages.txt)");

  for (auto p: packages) {
    fout<<p.toString()<<endl;
  }
  fout.close();
  // LoadData();
  this->notify();
}

void Repository::deliverPackage(Courier c, int index) {
  Package p = getUndeliveredAssigned(c)[index];
  p.setStatus("true");
  vector<Package> undelivered;
  undelivered.push_back(p);
for (auto pack: packages) {
  if (pack.getRecipient() != p.getRecipient() || pack.getStr() != p.getStr()) {
    undelivered.push_back(pack);
  }
}
  packages=undelivered;
  writeToFile();
  LoadData();
  vector<Observer*> obs = observers;
  this->notify();

}