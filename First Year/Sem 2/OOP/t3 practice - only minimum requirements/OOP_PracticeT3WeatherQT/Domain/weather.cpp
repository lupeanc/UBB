
#include "weather.h"

weather::weather(){}
weather::weather(int start, int end, int pp, string description){
  this->start = start;
  this->end = end;
  this->pp = pp;
  this->description = description;
}
weather::~weather(){}

int weather::getStart(){
  return this->start;
}

int weather::getEnd(){
  return this->end;
}

int weather::getPp(){
  return this->pp;
}

string weather::getDescription(){
  return this->description;
}

string weather::toString(){
  string weather;
  weather = to_string(start) + " " + to_string(end) + " " + to_string(pp) + " " + description + "\n";
  return weather;
}