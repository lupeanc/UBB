
#include "Department.h"
Department::Department(){}
Department::Department(string name, string desc1, string desc2, string desc3, string desc4, string desc5){
  this->name=name;
  this->desc1=desc1;
  this->desc2=desc2;
  this->desc3=desc3;
  this->desc4=desc4;
  this->desc5=desc5;
}
string Department::getName(){
  return name;
}
string Department::getDesc1(){
  return desc1;
}
string Department::getDesc2(){
  return desc2;
}
string Department::getDesc3(){
  return desc3;
}
string Department::getDesc4(){
  return desc4;
}
string Department::getDesc5(){
  return desc5;
}

string Department::getDescription() {
  return desc1+ " " + desc2 + " " + desc3 + " " + desc4 + " " + desc5;
}
