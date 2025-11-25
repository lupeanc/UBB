
#include "Dishwasher.h"
Dishwasher::Dishwasher(){}
Dishwasher::Dishwasher(string id, double consumedElecHour){
  this->id = id;
  this->consumedElecHour = consumedElecHour;
  }

// double Dishwasher::getConsumedElecHour(){
//   return this->consumedElecHour;
// }

string Dishwasher::toString(){
  string str =this->id + " Dishwasher " + to_string(this->consumedElecHour);
  return str;
}

Dishwasher::~Dishwasher(){}