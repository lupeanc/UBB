
#include "Person.h"
// Person::Person() {
//
// }
// Person::Person(string name) {
//   this->name = name;
// }

void Person::addRepo(Measurement* measurement) {
  measurements.push_back(measurement);
}

void Person::setName(string nameNew){
  this->name = nameNew;
}

string Person::getName(){
  return this->name;
}

void Person::initRepo() {
  Measurement* measurement = new BMI("1", 2.1);
  this->addRepo(measurement);
  Measurement* measurement2 = new BP("2", 2, 3);
  this->addRepo(measurement2);
}

vector<Measurement*> Person::getRepo() {
  return measurements;
}

// Person::~Person() = default;
