
#include "Refrigerator.h"
#include <iostream>
using namespace std;

Refrigerator::Refrigerator() {}
Refrigerator::Refrigerator(string id, string usageClass, bool hasFreezer){
        this->id = id;
        this->usageClass = usageClass;
        this->hasFreezer = hasFreezer;
}

// string Refrigerator::getUsageClass(){
//   return this->usageClass;
// }
// bool Refrigerator::getHasFreezer(){
//   return this->hasFreezer;
// }

string Refrigerator::toString(){
  string str = this->id + " Refrigerator " + this->usageClass;
  if(this->hasFreezer){
    str += " true";
  }
  else
    str += " false";
  return str;
}

Refrigerator::~Refrigerator() {}