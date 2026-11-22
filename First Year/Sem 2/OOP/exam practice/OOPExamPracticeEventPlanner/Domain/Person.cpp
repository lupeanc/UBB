
#include "Person.h"

string Person::toString(){
  return name + " " + to_string(xloc) + " " + to_string(yloc) + " " + to_string(status);
}