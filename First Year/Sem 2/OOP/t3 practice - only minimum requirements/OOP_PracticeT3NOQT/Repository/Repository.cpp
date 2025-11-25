
#include "Repository.h"
#include <fstream>

void Repository::LoadData(){
  ifstream fin(R"(F:\\c projects uni\\OOP_PracticeT3NOQT\\input.txt)");

  int start, end, pp;
  string description;

  this->elements.clear();

  while(fin>>start>>end>>pp>>description){
    Weather currentElement(start,end,pp, description);
    this->elements.push_back(currentElement);
  }

  fin.close();
}

Repository::Repository(){
  this->LoadData();
}

vector<Weather> Repository::getAll(){
  return this->elements;
}

Repository::~Repository(){}
