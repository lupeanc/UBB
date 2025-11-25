
#include "Doctor.h"
Doctor::Doctor(){}

Doctor::Doctor(string name, string specialization){
  this->name = name;
  this->specialization = specialization;

}

string Doctor::getName(){
  return name;
}

string Doctor::getSpecialization(){
  return specialization;
}