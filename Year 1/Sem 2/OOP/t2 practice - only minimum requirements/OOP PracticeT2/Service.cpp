
#include "Service.h"
Service::Service(Repo repo){}

vector<Appliance*> Service::getAllRepo(){
  return repo.getAllRepo();
}
void Service::addAppliance(Appliance* appliance){
  repo.addRepo(appliance);
}