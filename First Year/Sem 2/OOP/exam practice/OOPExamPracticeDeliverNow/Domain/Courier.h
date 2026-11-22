
#ifndef COURIER_H
#define COURIER_H
#include<iostream>
#include "Zone.h"
using namespace std;



class Courier {
  private:
    string name, st1, st2, st3;
    Zone zone;

    public:
      Courier(){}
      Courier(string name, string st1, string st2, string st3, Zone zone){
        this->name = name;
        this->st1 = st1;
        this->st2 = st2;
        this->st3 = st3;
        this->zone = zone;
      }
      string getName(){
        return name;
      }
      string getSt1(){
        return st1;
      }
      string getSt2(){
        return st2;
      }
      string getSt3(){
        return st3;
      }
      string toString();
      ~Courier()=default;

};



#endif //COURIER_H
