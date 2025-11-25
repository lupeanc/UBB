
#include "BMI.h"
BMI::BMI(){}
BMI::BMI(string date, double val){
  this->date=date;
  this->val=val;
}
string BMI::toString(){
  string str;
  str=date+" "+to_string(val);
  return str;
}
BMI::~BMI(){}