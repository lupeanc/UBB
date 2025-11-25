
#ifndef DRIVER_H
#define DRIVER_H
#include<iostream>
using namespace std;


class Driver {
  private:
    string name;
    int xloc, yloc, score;

    public:
      Driver(){};
      Driver(string n, int xloc, int yloc, int score){
        this->name = n;
        this->xloc = xloc;
        this->yloc = yloc;
        this->score = score;
      }
      string toString(){
        return name+ " " + to_string(xloc) + " " + to_string(yloc) + " " + to_string(score);
      }
      string getName(){
        return name;
      }
      string getAllStr() {
        return to_string(xloc) + " " + to_string(yloc) + " " + to_string(score);
      }
      int getXloc() {
        return xloc;
      }
  int getYloc() {
        return yloc;
      }
      ~Driver()=default;

};



#endif //DRIVER_H
