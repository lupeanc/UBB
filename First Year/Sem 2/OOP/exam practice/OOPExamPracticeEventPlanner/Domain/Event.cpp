
#include "Event.h"

string Event::toString(){
  return organiser + " " + name + " " + desc + " " + to_string(xloc) + " " + to_string(yloc) + " " + date;
}

string Event::toStringWindow(){
  return organiser + " " + name + " " + to_string(xloc) + " " + to_string(yloc) + " " + date;
}