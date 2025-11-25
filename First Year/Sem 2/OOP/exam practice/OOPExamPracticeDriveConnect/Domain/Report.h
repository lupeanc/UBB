
#ifndef REPORT_H
#define REPORT_H
#include<iostream>
using namespace std;


class Report {
  private:
    string desc, name;
    int xloc, yloc;
    bool status;

    public:
      Report(){};
      Report(string desc, string name, int xloc, int yloc, bool status){
        this->desc = desc;
        this->name = name;
        this->xloc = xloc;
        this->yloc = yloc;
        this->status = status;
      }
      bool getStatus(){
        return status;
      }
      int getXloc() {
        return xloc;
      }
  int getYloc() {
        return yloc;
      }
      string toString();


};



#endif //REPORT_H
