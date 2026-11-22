
#include "Surgery.h"
Surgery::Surgery(){}
Surgery::Surgery(string name, int nbDr, int nbPatients){
  this->nbPatients = nbPatients;
  this->nbDr = nbDr;
  this->name = name;
}
string Surgery::toString(){
  string str;
  str = "Surgery - Patients: " + to_string(nbPatients) + " - Nb Dr: " + to_string(nbDr);
  return str;
}
Surgery::~Surgery(){}