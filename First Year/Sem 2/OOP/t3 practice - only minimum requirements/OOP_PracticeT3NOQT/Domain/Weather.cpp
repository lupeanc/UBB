
#include "Weather.h"

Weather::Weather(){};
Weather::~Weather(){};
Weather::Weather(int start, int end, int pp, string description){
  this->start = start;
  this->end = end;
  this->pp = pp;
  this->description = description;
}

int Weather::getStart(){
  return this->start;
}

int Weather::getEnd(){
  return this->end;
}

int Weather::getPp(){
  return this->pp;
}

string Weather::getDescription(){
  return this->description;
}