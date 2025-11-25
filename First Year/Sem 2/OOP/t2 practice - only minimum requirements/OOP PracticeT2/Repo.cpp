
#include "Repo.h"


void Repo::addRepo(Appliance* appliance){
  this->appliances.push_back(appliance);
}

void Repo::init(){
  Appliance* appliance1 = new Refrigerator("12", "A", true);
  this->addRepo(appliance1);
  Appliance* appliance2 = new Dishwasher("34", 2.1);
  this->addRepo(appliance2);
}

vector<Appliance*> Repo::getAllRepo(){
  return this->appliances;
}