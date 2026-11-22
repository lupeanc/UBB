
#include "Volunteer.h"
Volunteer::Volunteer(){
}
Volunteer::~Volunteer(){}
Volunteer::Volunteer(string name, string email, string i1, string i2, string i3, string department){
  this->name = name;
  this->email = email;
  this->i1 = i1;
  this->i2 = i2;
  this->i3 = i3;
  this->department = department;
}
string Volunteer::getName(){
  return name;
}
string Volunteer::getEmail(){
  return email;
}
string Volunteer::getI1(){
  return i1;
}
string Volunteer::getI2(){
  return i2;
}
string Volunteer::getI3(){
  return i3;
}
string Volunteer::getDepartment(){
  return department;
}

string Volunteer::toString() {
  return name+ " " + email + " " + i1 + " " + i2 + " " + i3 + " " + department;
}
