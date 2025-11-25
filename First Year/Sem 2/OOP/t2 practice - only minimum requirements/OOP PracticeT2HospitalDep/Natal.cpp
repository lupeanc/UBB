
#include "Natal.h"
Natal::Natal() {}
Natal::Natal(string name, int nbDr, int nbMothers, int nbNewborns){
  this->nbMothers = nbMothers;
  this->nbNewborns = nbNewborns;
  this->name = name;
  this->nbDr = nbDr;
}

string Natal::toString(){
  string str;
  str = "Natal - NbMothers: " + to_string(nbMothers) + " NbNewborns: " + to_string(nbNewborns) + " - Nb Dr: " + to_string(nbDr);
  return str;
}

Natal::~Natal() {}