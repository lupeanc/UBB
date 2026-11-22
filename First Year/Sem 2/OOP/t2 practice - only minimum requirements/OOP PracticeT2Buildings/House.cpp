
#include "House.h"
House::House(){}
House::House(string address, int constrYear, string type, bool historical){
  this->address = address;
  this->constrYear = constrYear;
  this->type = type;
  this->historical = historical;
}

string House::toString() {
  string str;
  if (historical) {
    str = "Address: " + address + " Constr Year: " + to_string(constrYear) + "Type: " + type + "Historical: true";
  }
  else
    str = "Address: " + address + " Constr Year: " + to_string(constrYear) + "Type: " + type + "Historical: false";
  return str;
}

House::~House()= default;