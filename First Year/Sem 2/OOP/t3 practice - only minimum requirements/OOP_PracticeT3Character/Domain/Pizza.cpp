
#include "Pizza.h"

Pizza::Pizza(){}
Pizza::~Pizza(){}
Pizza::Pizza(int slices, string toppings){
  this->slices = slices;
  this->toppings = toppings;
}

string Pizza::getToppings(){
  return toppings;
}

string Pizza::toString(){
  string str;
  str = to_string(slices) + " " + toppings;
  return str;
}