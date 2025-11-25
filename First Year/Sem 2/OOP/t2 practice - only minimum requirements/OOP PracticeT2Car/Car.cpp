
#include "Car.h"
Car::Car(){}
Car::Car(string bodyStyle, Engine* engine){
  this->bodyStyle = bodyStyle;
  this->engine = engine;
}

string Car::toString(){
  string str;
  str = "Body: " + bodyStyle + engine->toString() + "\n";
  return str;
}