
#include "BP.h"
BP::BP(){}
BP::BP(string date, int sistval, int diasval){
  this->date=date;
  this->sistval=sistval;
  this->diasval=diasval;
}

string BP::toString(){
  string str;
  str=date+" "+to_string(sistval)+" "+to_string(diasval);
  return str;
}

BP::~BP(){}