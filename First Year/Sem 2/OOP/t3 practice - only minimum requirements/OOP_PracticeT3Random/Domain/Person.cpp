
#include "Person.h"

Person::Person(){}

Person::Person(string name, int age){
  this->name = name;
  this->age = age;
}

string Person::toString(){
  string str;
  str = name + " " + to_string(age);
  return str;
}

string Person::getName(){
  return name;
}

Person::~Person(){}