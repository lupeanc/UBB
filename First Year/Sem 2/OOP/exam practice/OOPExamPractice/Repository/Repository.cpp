
#include "Repository.h"
#include <fstream>

Repository::Repository(){
  this->LoadData();
}

Repository::~Repository(){}

void Repository::LoadData() {
  ifstream fin(R"(F:\\c projects uni\\OOP_PracticeT3WeatherQT\\input.txt)");
  int start, end, pp;
  string description;

  this->elements.clear();

  while(fin>>start>>end>>pp>>description){
    weather w(start,end,pp,description);
    elements.push_back(w);
  }

  fin.close();

}

vector<weather> Repository::getAll(){
  return this->elements;
}
