
#include "Turbo.h"
Turbo::Turbo(){}
Turbo::Turbo(double price){
  this -> price = price;
}
double Turbo::getPrice(){
  return price;
}

string Turbo::toString(){
  string str;
  str = " Price: " + to_string(price) + "\n";
  return str;
}

Turbo::~Turbo(){}