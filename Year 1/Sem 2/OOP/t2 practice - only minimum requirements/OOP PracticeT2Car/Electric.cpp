
#include "Electric.h"
Electric::Electric(){}
Electric::Electric(double price, int autonomy){
  this->price = price;
  this->autonomy = autonomy;
}
double Electric::getPrice(){
  return price;
}
string Electric::toString(){
  string str;
  str = " Price: " + to_string(price) + " Autonomy: " + to_string(autonomy) + "\n";
  return str;
}
Electric::~Electric(){}