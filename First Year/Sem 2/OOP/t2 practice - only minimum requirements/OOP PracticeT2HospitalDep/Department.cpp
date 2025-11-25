
#include "Department.h"

string Department::getName(){
  return name;
}

int Department::getNbDr(){
  return nbDr;
}

void Department::setName(string nameNew){
  this->name = nameNew;
}

void Department::setNbDr(int nbDrNew){
  this->nbDr = nbDrNew;
}