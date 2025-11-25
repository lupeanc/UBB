
#include "Controller.h"
void Controller::addBuilding(Building* building) {
  buildings.push_back(building);
}
void Controller::initController(){
  Building* building = new House( "adr", 1987, "old", true);
  addBuilding(building);
  Building* building2 = new Block( "adr", 1987, 18, 9);
  addBuilding(building2);
}
vector<Building*> Controller::getBuildings(){
  return buildings;
}