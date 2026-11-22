#include <fstream>
#include "Repository.h"
#include <algorithm>

Repository::Repository(){
  this->LoadData();
}

void Repository::LoadData(){
  ifstream fin(R"(F:\\c projects uni\\OOP_PracticeT3Random\\input.txt)");
  string name;
  int age;

  elements.clear();

  while(fin >> name >> age){
    Person person(name, age);
    elements.push_back(person);
  }

  fin.close();

}

bool compare(Person p1, Person p2){
  return p1.getName() < p2.getName();
}

vector<Person> Repository::getAll(){
//  return elements;
    std::sort(elements.begin(), elements.end(), compare);
    return elements;
}

Repository::~Repository(){}